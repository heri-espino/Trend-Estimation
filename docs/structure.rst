Project structure
=================

Library
-------

`src/trend_estimation/` is the installable package. Reusable mathematics,
models, selectors, validation logic, metrics, simulation generators, and plots
belong there.

Documentation
-------------

`docs/` is the Sphinx documentation. Users should be able to find public
functions and classes here without opening source files.

Research notes
--------------

`notes/` contains derivations, checkpoints, unresolved questions, and the
internal roadmap. These are working scientific notes, not API docs.

Papers and experiments
----------------------

`paper_<short-title>/` contains manuscript-specific text.

`experiments/<short_title>/` contains reproducible experiment drivers that
import `trend_estimation`. Reusable algorithms must stay in the library.

Clean-main policy
-----------------

Historical reports, obsolete manuscript folders, copied legacy scripts, and
empty placeholder namespaces are not kept on `main`. Git history is the
archive.
