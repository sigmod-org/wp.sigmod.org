#!/usr/bin/env python3
"""Generate index.html and 404.html: the "blog has moved" page with old-URL redirects.

The old WordPress blog used "plain" permalinks on the site root (/?p=3855,
/?cat=16, ...), and static hosting ignores query strings, so both pages carry a
small script that maps old URLs to the new blog. The map is read from the
blog's imported files (wp_id in each post/page, _data/authors.yml,
_data/categories.yml), so re-run this after importing:

    python3 tools/build_redirects.py [--blog ../blog.sigmod.org]

NEW_BLOG below is the new blog's address.
"""

import argparse
import glob
import html
import json
import os
import re

NEW_BLOG = "https://blog.sigmod.org/"
DELAY = 10  # seconds before the landing page sends visitors to the new blog

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def front_matter(path):
    text = open(path, encoding="utf-8").read(4000)
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    return dict(re.findall(r'^(\w+):\s*"?([^"\n]*)"?\s*$', m.group(1), re.M)) if m else {}


def yaml_ids(path):
    """slug -> wp_id from the importer's flat YAML maps."""
    ids, slug = {}, None
    for line in open(path, encoding="utf-8"):
        if m := re.match(r'^"?([^"\s:#][^":]*)"?:\s*$', line):
            slug = m.group(1)
        elif (m := re.match(r"^\s+wp_id:\s*(\d+)", line)) and slug:
            ids[m.group(1)] = slug
    return ids


def build_map(blog):
    posts = {}
    for path in glob.glob(os.path.join(blog, "_posts", "*")) + glob.glob(os.path.join(blog, "_pages", "*")):
        fm = front_matter(path)
        if fm.get("wp_id") and fm.get("permalink"):
            posts[fm["wp_id"]] = fm["permalink"].lstrip("/")
    # Only categories and authors that have a page on the new blog.
    cats = {i: f"category/{s}/" for i, s in yaml_ids(os.path.join(blog, "_data", "categories.yml")).items()
            if os.path.exists(os.path.join(blog, "category", s + ".html"))}
    authors = {i: f"author/{s}/" for i, s in yaml_ids(os.path.join(blog, "_data", "authors.yml")).items()
               if os.path.exists(os.path.join(blog, "author", s + ".html"))}
    return {"posts": posts, "cats": cats, "authors": authors}


SCRIPT = r"""
(function () {
  var blog = %(blog)s, map = %(map)s;
  var q = new URLSearchParams(location.search), go = null, m;
  // Path below the site root (strip /<repo> while served from *.github.io).
  var path = location.pathname;
  if (/\.github\.io$/.test(location.hostname)) path = path.replace(/^\/[^\/]+/, "");
  var id = q.get("p") || q.get("page_id");
  if (/^\/wp-content\/uploads\//.test(path)) go = path.slice(1);  // images are mirrored
  else if (id) go = map.posts[id] || "archives/";
  else if (q.get("cat")) go = map.cats[q.get("cat")] || "archives/";
  else if (q.get("author_name")) go = Object.values(map.authors).indexOf("author/" + q.get("author_name") + "/") >= 0
      ? "author/" + q.get("author_name") + "/" : "archives/";
  else if (q.get("author")) go = map.authors[q.get("author")] || "archives/";
  else if ((m = /^(\d{4})(\d{2})?/.exec(q.get("m") || ""))) go = "archives/#" + m[1] + (m[2] ? "-" + m[2] : "");
  else if (q.has("feed")) go = "feed.xml";
  else if (q.has("s")) go = "search/?q=" + encodeURIComponent(q.get("s"));
  // Old deep links go straight to their new page; everything else gets the notice.
  // Keep #comment-N anchors: archived comments carry the same ids on the new blog.
  if (go !== null) { location.replace(blog + go + (go.indexOf("#") < 0 ? location.hash : "")); return; }
  var left = %(delay)d, el = document.getElementById("countdown");
  setInterval(function () {
    if (--left <= 0) location.replace(blog);
    else el.textContent = left + (left === 1 ? " second" : " seconds");
  }, 1000);
})();
"""

PAGE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>The ACM SIGMOD Blog has moved</title>
  <meta name="description" content="The ACM SIGMOD Blog now lives at {blog_text}.">
  <link rel="canonical" href="{blog}">
  <noscript><meta http-equiv="refresh" content="{delay};url={blog}"></noscript>{robots}
  <link rel="icon" href="{blog}favicon.ico" sizes="any">
  <link rel="icon" href="{blog}favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="{blog}apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Newsreader:opsz,wght@6..72,500;6..72,600&display=swap" rel="stylesheet">
  <style>
    /* Same look as the new blog (blog.sigmod.org/assets/css/main.css). */
    :root {{
      --page-bg: #dddddd; --box-bg: #ffffff; --band-bg: #f7f7f9; --text: #424242;
      --heading: #000000; --rule: #e2e2e2; --accent: #23177a; --link: #2f3fb5;
      --footer-bg: #222222; --footer-text: #bbbbbb; --content-bg: #f0f0f2;
      --sigmod-blue: #1f4fa3; --sigmod-blue-hover: #173d80;
      --heading-font: "Newsreader", Georgia, serif;
      --body-font: "Inter", system-ui, sans-serif;
    }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; background: var(--page-bg); color: var(--text); font: 400 17px/1.65 var(--body-font);
      -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; }}
    a {{ color: var(--link); }}
    .page {{ max-width: 1080px; margin: 0 auto; min-height: 100vh; display: flex; flex-direction: column;
      background: var(--box-bg); box-shadow: 0 0 10px rgba(0,0,0,.2); }}
    .container {{ width: 80%; max-width: 1080px; margin: 0 auto; }}
    header {{ height: 80px; display: flex; align-items: center; box-shadow: 0 1px 0 rgba(0,0,0,.1); }}
    header img {{ display: block; }}
    .band {{ background: var(--band-bg); border-bottom: 1px solid var(--rule); padding: 26px 0 22px; }}
    .band p {{ margin: 0; font: 500 26px/1.2 var(--heading-font); color: var(--heading); }}
    main {{ flex: 1; padding: 40px 0 64px; background: var(--content-bg); }}
    .box {{ background: var(--box-bg); border: 1px solid #e5e7eb; border-bottom: 2px solid var(--accent);
      border-radius: 10px; box-shadow: 0 10px 30px -18px rgba(17,24,39,.35); padding: 32px 38px 34px; }}
    h1 {{ font: 600 34px/1.2 var(--heading-font); letter-spacing: -0.01em; color: var(--accent); margin: 0 0 20px; }}
    .new-url {{ font-size: 20px; font-weight: 600; word-break: break-all; }}
    .button {{ display: inline-block; margin-top: 12px; padding: 10px 16px; background: var(--sigmod-blue); color: #fff;
      font: 600 14px/1 var(--body-font); border-radius: 999px; text-decoration: none; }}
    .button:hover {{ background: var(--sigmod-blue-hover); }}
    .small {{ font-size: 14px; color: #666; }}
    footer {{ background: var(--footer-bg); color: var(--footer-text); font-size: 14px; padding: 16px 0; }}
    footer a {{ color: #fff; }}
    @media (max-width: 560px) {{ .container {{ width: auto; margin: 0 16px; }} h1 {{ font-size: 28px; }}
      .box {{ padding: 22px 18px 24px; }} }}
  </style>
</head>
<body>
<div class="page">
  <header><div class="container">
    <a href="{blog}"><img src="{blog}assets/img/sigmod-logo.png" alt="ACM SIGMOD" width="140" height="45"></a>
  </div></header>
  <div class="band"><div class="container"><p>ACM SIGMOD Blog</p></div></div>
  <main><div class="container"><div class="box">
    <h1>The ACM SIGMOD Blog has moved</h1>
    <p>The blog, with all of its posts, now lives at</p>
    <p class="new-url"><a href="{blog}">{blog_text}</a></p>
    <p>Please update your links and bookmarks.</p>
    <p class="small">You will be taken there automatically in <span id="countdown">{delay} seconds</span>.</p>
    <a class="button" href="{blog}">Go to the new blog now</a>
  </div></div></main>
  <footer><div class="container">&copy; ACM SIGMOD &middot; <a href="https://sigmod.org">sigmod.org</a></div></footer>
</div>
<script>{script}</script>
</body>
</html>
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--blog", default=os.path.join(HERE, "..", "blog.sigmod.org"),
                    help="checkout of the new blog (default: ../blog.sigmod.org)")
    args = ap.parse_args()
    data = build_map(os.path.abspath(args.blog))
    script = SCRIPT % {"blog": json.dumps(NEW_BLOG), "map": json.dumps(data, sort_keys=True), "delay": DELAY}
    for name, robots in (("index.html", ""), ("404.html", '\n  <meta name="robots" content="noindex">')):
        page = PAGE.format(blog=html.escape(NEW_BLOG), blog_text=html.escape(NEW_BLOG.split("://")[1].rstrip("/")),
                           delay=DELAY, robots=robots, script=script)
        open(os.path.join(HERE, name), "w", encoding="utf-8").write(page)
    print(f"{len(data['posts'])} posts/pages, {len(data['cats'])} categories, "
          f"{len(data['authors'])} authors -> index.html, 404.html")


if __name__ == "__main__":
    main()
