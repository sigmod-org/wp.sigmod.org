# wp.sigmod.org

The old WordPress home of the ACM SIGMOD Blog. The blog has moved to
**<https://sigmod-org.github.io/blog.sigmod.org/>**
([sigmod-org/blog.sigmod.org](https://github.com/sigmod-org/blog.sigmod.org));
this repository holds everything that concerns the old site, so the blog itself
does not have to.

## The "blog has moved" site

`index.html` and `404.html` (served by GitHub Pages; plain static files) show a
notice asking visitors to update their links, then send them to the new blog
after 10 seconds. Old deep links go straight to their new page:

| Old URL                           | Goes to (on the new blog)        |
| --------------------------------- | -------------------------------- |
| `/?p=3855`, `/?page_id=2`         | the imported post / page         |
| `/?cat=16`                        | `/category/databases/`           |
| `/?author_name=x`, `/?author=120` | `/author/x/`                     |
| `/?m=202609`                      | `/archives/#2026-09`             |
| `/?feed=rss2`                     | `/feed.xml`                      |
| `/?s=query`                       | `/search/?q=query`               |
| `/wp-content/uploads/...`         | same path (images are mirrored)  |

Unknown post, category or author IDs go to the archives; anything else gets the
notice. Both pages are generated, with the ID map inlined, from a checkout of
the blog next to this one:

```bash
python3 tools/build_redirects.py          # --blog ../blog.sigmod.org
```

Re-run it after importing more posts. The new blog's address and the delay are
`NEW_BLOG` and `DELAY` at the top of the script.

For old links to keep working, point the `wp.sigmod.org` DNS at GitHub Pages and
set it as this repository's custom domain (*Settings → Pages*), once the
WordPress site is no longer needed. When the blog gets its own domain, update
`NEW_BLOG` and re-run the script.

## Importing from WordPress

These need the WordPress site online (they use its public REST API, no
credentials). Both write into the blog checkout (`--blog`, default
`../blog.sigmod.org`):

```bash
python3 tools/wp_import.py --latest 1        # newest post
python3 tools/wp_import.py --post 3855       # specific post IDs
python3 tools/wp_import.py --page 2 3873     # specific page IDs (About, Editors)
python3 tools/wp_import.py --all             # every published post
python3 tools/audit_posts.py                 # writes IMPORT_REVIEW.md here
```

The importer is idempotent (files are keyed by WordPress ID) and:

- writes posts to `_posts/` as raw WordPress HTML, pages to `_pages/`;
- mirrors images to `wp-content/uploads/...` at their **original paths**;
- records authors in `_data/authors.yml` and all WordPress categories in
  `_data/categories.yml`, and creates `category/<slug>` and `author/<slug>` pages;
- rewrites links between imported posts to their new URLs, and resolves
  `?attachment_id=` / `?cat=` links and Google Docs redirect links;
- keeps local copies of images pasted from Google Docs (`wp-content/uploads/external/`);
- cleans up old-WordPress markup: one-column layout tables, unclosed `<div>`s,
  `http://` embeds.

Files with `keep_local_edits: true` in their front matter (e.g. the About page) are
never overwritten unless `--force` is given. Comments have not been migrated.

[IMPORT_REVIEW.md](IMPORT_REVIEW.md) lists imported posts flagged for a check by
eye, with the verdicts so far.
