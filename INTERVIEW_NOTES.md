# INTERVIEW QUESTIONS

## Round 1

What initial files should be created in the kodi.script.module.auth0-ciam-client directory to establish the basic Kodi addon structure, such as addon.xml, and how will they reference the bundled auth0_ciam_client code?
> addon.xml, README.md, CHANGELOG.md (following makeachangelog spec), .gitignore, LICENSE.txt, pyproject.toml (if needed)

How will the auth0_ciam_client package be copied or linked into the addon's resources/lib/ directory without altering the original, and what build or sync process will ensure updates are reflected?
> for local development, we can symlink it over.  In production, the github ci process should either check out or pip-instlal the python for bundling.

For the addon.xml, what specific metadata (e.g., id, name, version, description, author) will be set, and how will dependencies like script.module.requests be declared?
> I have added an addon.xml to reference

What Kodi-specific elements, if any, need to be added to the bundled code (e.g., imports or compatibility shims) while keeping the original unmodified?
> Good question.  none come to mind.,  the only "hack" currently in place is the logging allowance such that logs are bubbled up in a KODI-friendly
> manner.  Should this be a "modification" for this bundler, and we revert the pythoin library to more standard logging?  Would be open to discussion on this

How will the addon's README.md differ from the library's, focusing on Kodi installation and usage rather than general Python integration?
> yes, README should be just about KODI.  I assum ewe can follow patterns used by script.module.reqeusts.

What testing approach will be used for the addon, such as running the existing unit tests within a Kodi environment or using Kodi's addon testing tools?
> UNit test should be run if there are modifications made to the code.  kodi-addon-checker should definitely be run.

For versioning, how will the addon's initial version relate to the library's current version, and what tagging strategy will be applied in the new repo?
> I am open to suggestions on this point.

What potential Kodi compatibility issues (e.g., Python version differences) should be addressed in the addon without changing the library?
> the library ought to support all the python vrsion that KODI supports for Nexus and beyond (3.9+).  No differences here.

How will documentation for addon developers be structured, including examples of importing and using the module in other Kodi addons?
> not sure.  open to suggestions.

What are the key submission requirements from the Kodi repository that need to be incorporated from the start, such as licensing or changelog formats?
> changelog should follow makeachangelog pattern.

For the migration in Angel Studios, what exact changes will be needed in its code to switch from bundling to depending on this addon?
> no migration concerns.  we have not yet hit a 1.0.0 release, so breaking hcanges are fine for now.

What fallback or error handling should the addon include if Kodi-specific features (e.g., logging) are unavailable, to maintain library compatibility?
> im not sure what this means.  we should dive more into this topic.

How can the addon be designed to support future extensions, like additional auth flows, without modifying the core library?
> would be open to suggestions on this.  you mean something besides our current user/pass flow?

What CI/CD setup will be established for the addon repo, separate from the library's, to handle builds and releases?
> CI/CD will consist of kodi-sopecific checks and the zipfile release process.

Considering the 90% test coverage goal, how will tests be adapted or added specifically for the addon context, such as integration with Kodi's import system?
> UNsure what you mean by this.

What user-facing aspects, if any, will the addon expose (e.g., settings), and how will they be implemented without altering the library?
> None.  The addons using this module will provide all that themselves.  this is just a module.

For internationalization, what preparations should be made in the addon for potential translations, even if the library is English-only?
> unknown

What monitoring or analytics will be included post-release to track addon usage or issues in the Kodi ecosystem?
> i have no idea how any of that works.  suggestions?

What are the tradeoffs of bundling the entire library versus selectively including only necessary files to keep the addon size minimal?
> currently the entire library is fairly small, so im not worried about that yet.  we ought to make sure we do not have
> extraneous items such as pychace and the like, however.  a clean zip at the end is the goal. ref. script.module.requests.

How will security considerations, like token handling, be ensured in the addon distribution without exposing vulnerabilities?
> explain concerns in depth here.  The user oif the library is responsible for security at that level, i woudl think

## Round 2

For the logging "hack" mentioned (bubbling up logs in a Kodi-friendly manner), should the Python library be reverted to standard logging, and if so, how would the addon handle Kodi integration (e.g., via xbmc.log wrappers) without modifying the library?
> It would seen this is the better path.  Is there a good pattern for capuring "standard" logs and making the KODI Logs?

On versioning, what initial version number should the addon start with (e.g., 1.0.0 to match the library, or 0.1.0 for pre-release), and how will tags be structured (e.g., v1.0.0 for releases, with semver)?
> Our first goal will be a function 0.1.0, which ought to match the library.  I believe keeping them in sync is best, but would like to hear more about other
> existing patterns for this.

For documentation structure, what format and content would work best—e.g., inline comments in the bundled code, a separate wiki, or examples in the README showing Kodi addon imports like from resources.lib.auth0_ciam_client import Core?
> commnets in code and README.  No need for a wiki at this point.

Regarding fallback/error handling for Kodi-specific features, what scenarios are you envisioning (e.g., if xbmc is not available outside Kodi), and how should the addon detect and adapt (e.g., falling back to print statements)?
> the module addon should only ever run within kodi.  what scenarios are you envisioning here?

For future extensions like additional auth flows, what interfaces or hooks could be added to the addon (e.g., a plugin system for custom providers) without touching the library?
> none that i can think of

On CI/CD, what specific tools or scripts will handle the Kodi checks (e.g., kodi-addon-checker) and zipfile creation, and how will releases be automated?
> I have a release.yml in another project that I will bring over as a base.

For test coverage in the addon context, what do you mean by "integration with Kodi's import system"—e.g., testing that the module loads correctly in Kodi's Python environment?
> yes.  we assume the library itself already has all the necessary unit tests passing, so i dont think we need to test that again.  just
> whatever additions we make (e.g. to wrap the logging) should be tested here, and any KODI-specific tests.

For internationalization preparations, even if minimal, what files or placeholders (e.g., strings.po) should be included for future translations?
> I do not know how this is normally handled in script modules.  can you check `requests`?

On monitoring/analytics, what options exist in Kodi (e.g., addon update checks or user feedback via forums), and how could issue tracking be set up?
> None that im aware of.  needs rtesearch.

For security considerations in token handling, what specific risks (e.g., token leakage in logs, insecure storage) should be mitigated, and how (e.g., avoiding sensitive data in exceptions)?
> this bundler should not make any changes to how logs are handled.  security should exist fo the library itself, and any
> downstream consumers should have their own security.  are you asking about this bundler specifically, or for the library?

What exact changes or additions are needed in the addon.xml beyond what's already added, such as platform restrictions or changelog links?
> what are my options?

How will the GitHub CI process for bundling (e.g., checking out or pip-installing the library) be configured to ensure clean, reproducible builds?
> unknown what you mean by this

For the README, what patterns from script.module.requests should be followed—e.g., installation instructions via Kodi repo, usage examples, or dependency notes?
> what is standard here?

What does "no migration concerns" for Angel Studios mean in terms of timeline or compatibility—e.g., will it switch immediately or gradually?
> we are not near a 1.0.0 stable release.  So breaking changes for now are fine.  when the library reaches 1.0.0 we should address
> migration concerns.

For the changelog following makeachangelog, what initial entries will be included, and how will it sync with the library's changelog?
> good question.  how would this normally be handled?

What "extraneous items" like pycache should be excluded from the addon zip, and how (e.g., via .gitignore or build scripts)?
> via .gitignore.  also a `make clean` would be useful (I like Makefiles for build processes.)

