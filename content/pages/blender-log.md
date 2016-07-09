Title: Blender Logs
## Current Branch : `*master*`
###Time Compiled : __7/10/2016, 6:17:21 AM__
***

# ~BLENDER


**AUTHOR** | **HASH** | **MESSAGE** | **TIME**
--- | --- | --- | ---
Lukas Stockner | `2a69b09` | Fix T48732 v2: New GGX breaks OpenCL kernel | *2 days ago*
Bastien Montagne | `aff81c6` | Cleanup: Get rid of remaining 'BKE_<id>_unlink()' functions, no more used anyway. | *2 days ago*
Bastien Montagne | `1b6cf7a` | Cleanup: get rid of BKE_text_unlink(), replace by usage of generic BKE_libblock_... API. | *2 days ago*
Bastien Montagne | `4287265` | Cleanup: remove RNA's `ID.destroy()` function. | *2 days ago*
Bastien Montagne | `d4e4358` | Cleanup/refactor RNA IDs' `remove` functions. | *2 days ago*
Campbell Barton | `bfcf8c8` | CMake: exclude gitignore & arcconfig for addons | *2 days ago*
Campbell Barton | `9c96585` | Cleanup: remove bad-level call | *2 days ago*
Campbell Barton | `0a99072` | GPU: move select index code out of WM | *2 days ago*
Jens Verwiebe | `28dbd57` | Exclude obsolete static pythonlibs from install | *2 days ago*
Thomas Dinges | `99088f8` | Fix T48732, OpenCL compile failure after Multiscatter GGX commit. | *2 days ago*
Campbell Barton | `05a60aa` | Fix T48723: Curve bevel creates invalid geometry | *2 days ago*
Campbell Barton | `8f0a44a` | Cleanup: use BLI_bitmap for bevel-split | *3 days ago*
Bastien Montagne | `c376ff2` | Fix T48725: UI message typo. | *3 days ago*
Campbell Barton | `a101175` | BMesh: avoid redundant calculations comparing angles | *3 days ago*
Campbell Barton | `73a9c56` | Fix T48716: Knife cut creates inverted normals | *3 days ago*
Campbell Barton | `823ab66` | Avoid memory leaks on exit during argument parsing | *4 days ago*
Campbell Barton | `25866aa` | BKE_blender: Add own atexit functions | *4 days ago*
Campbell Barton | `4fc1510` | Cleanup: use return argument prefix | *4 days ago*
Lukas Stockner | `23c2768` | Cycles: Add multi-scattering, energy-conserving GGX as an option to the Glossy, Anisotropic and Glass BSDFs | *4 days ago*
Joshua Leung | `2af4c80` | GPencil: Eraser respects "Selection Mask" when in EditMode | *4 days ago*
Joshua Leung | `9839aba` | Fix minor typo - Was m[3][4] instead of m[4][4] for a 4x4 matrix | *4 days ago*
Joshua Leung | `4fd78bb` | ChildOf Constraint: Hide the Loc/Rot/Scale toggles | *4 days ago*
Joshua Leung | `9466829` | DopeSheet Mask Mode: Circle/Lasso support | *4 days ago*
Joshua Leung | `833e69f` | DopeSheet: GPencil-Mode supports Circle and Lasso Select | *4 days ago*
Joshua Leung | `7e53f9f` | Dopesheet: Lasso and Circle Select tools work for selecting keyframes | *4 days ago*
Joshua Leung | `58acc18` | Code Cleanup - Circle/Lasso select in the Graph Editor | *4 days ago*
Joshua Leung | `b6a898b` | GPencil UI: Streamline toolbar options a bit | *4 days ago*
Joshua Leung | `ec7603d` | GPencil: Added a new version of the "delete active frame" operator which deletes on all editable layers | *4 days ago*
Bastien Montagne | `37560e7` | Fix T48689: Transform proportional size was not seriously clamped. | *4 days ago*
Campbell Barton | `d9a01a1` | Fix T48707: Edit-mesh intersect crash | *4 days ago*

***

# ~ADDONS


**AUTHOR** | **HASH** | **MESSAGE** | **TIME**
--- | --- | --- | ---
Bastien Montagne | `2b6a756` | Fix T48713: Problem when importing FBX file with 2 armatures. | *3 days ago*
Campbell Barton | `b196c48` | blendfile: add __repr__ to DNAName and DNAStruct | *5 days ago*
Campbell Barton | `a668b0b` | blendfile: fixed dna_type can't be indexed error | *5 days ago*
Campbell Barton | `5b03267` | blendfile: Python modules shouldn't set their own log level. | *5 days ago*
meta-androcto | `75fb4e0` | fix merge error reported in irc: add blocks file & correct references | *2 weeks ago*
meta-androcto | `eedce73` | Update mesh_extra_objects: T48640 | *2 weeks ago*
Bastien Montagne | `c4a7943` | Fix T48631: FBX setting "bake_anim_use_nla_strips": True, fails to export unique animations to each take. | *2 weeks ago*
Campbell Barton | `c82bb57` | minor edits to blendfile | *3 weeks ago*
Aaron | `aee180d` | Manual Ref: Fix links | *3 weeks ago*
Bastien Montagne | `f6cfb5b` | CLeanup: 'addon' -> 'add-on' in UI messages. | *4 weeks ago*
meta-androcto | `b7e87b9` | spacebar menu update, thanks @lijenstina | *4 weeks ago*
meta-androcto | `78e96f4` | update 3d view navigation: T48482 | *4 weeks ago*
Maurice Raybaud | `7e05091` | *converted all calls to file.write of .shading.py to tabWrite function to no longer pass the file variable | *5 weeks ago*
meta-androcto | `4eafe31` | Add Tab Name Change: T48459 | *5 weeks ago*
meta-androcto | `27a7811` | Fix panel category: T48459 | *5 weeks ago*

***

# ~ADDONS CONTRIB


**AUTHOR** | **HASH** | **MESSAGE** | **TIME**
--- | --- | --- | ---
meta-androcto | `686044b` | Rename ui_pie_menus/ to space_view3d_pie_menus update menu structure, clean up | *2 days ago*
meta-androcto | `6dbe6b8` | fix for auto keyframe thanks lijenstina | *6 days ago*
meta-androcto | `63dd75b` | pie menus: minor update | *7 days ago*
meta-androcto | `d181537` | fix for underscore in incremental file save, thanks lijenstina | *7 days ago*
meta-androcto | `1a654c4` | rewrite wazou pie menus (addons contrib) new menu & file structure | *8 days ago*
meta-androcto | `72c24a1` | update archimesh to correct version: T37230 | *2 weeks ago*
meta-androcto | `1886f83` | initial commit ui_wazou_pie_menus.py: T48618 | *2 weeks ago*
meta-androcto | `cbcbc78` | initial commit arrange_on_curve by Mano-Wii: T48622 | *2 weeks ago*
meta-androcto | `9968e89` | Initial Commit: Archimesh by antonioya: T37230 | *2 weeks ago*
meta-androcto | `9783a17` | remove add_mesh_building_objects made redundant by T48640 & T37230 | *2 weeks ago*
meta-androcto | `20619f3` | remove mesh_discombobulator.py (moved to release: T48640 | *2 weeks ago*
meta-androcto | `7c07ceb` | remove geodesic domes (moved to release): T48640 | *2 weeks ago*
meta-androcto | `7a2693b` | initial commit mesh_1D_scripts.py: T48619 | *2 weeks ago*
meta-androcto | `50f8d6d` | initial commit add_curve_simple.py: T37664 | *2 weeks ago*
meta-androcto | `810f8c4` | Contrib: Geodesic Domes > code clean up for T48608 | *2 weeks ago*

***

# ~BAM


**AUTHOR** | **HASH** | **MESSAGE** | **TIME**
--- | --- | --- | ---
Campbell Barton | `e6f6bd6` | minor edits to blendfile | *3 weeks ago*
Campbell Barton | `5f5baf3` | Minor changes | *5 months ago*
Campbell Barton | `4d6b5bf` | Use tuples for multi-part lookups | *5 months ago*
Campbell Barton | `d54c92b` | Cleanup: style | *5 months ago*
Bastien Montagne | `4360fa5` | bledfile.py: Port over changes from src_utils repo. | *5 months ago*
Campbell Barton | `5b0e517` | Improve subdirectory check | *6 months ago*
Campbell Barton | `5e9eb15` | Add 'bam copy' command. | *6 months ago*
Campbell Barton | `bd3173b` | Left in prints by accident | *6 months ago*
Eibriel | `f1e5d1d` | Fix 2 for T46811, wrong paths on .bam_paths_uuid | *6 months ago*
Eibriel | `3ab3dbf` | Adding BAM STATUS to test test_absolute_relative_from_blendfiles_texture | *6 months ago*
Bastien Montagne | `28429f2` | blendfile: "fix" blocks' iteration over values, and add 'user_data' member to Blocks and DNAStruct objects. | *7 months ago*
Campbell Barton | `693101d` | Adding test for bam_cli.py failing when missing texture on library | *7 months ago*
Campbell Barton | `4f322cf` | Fix T46811: Replaying binary edits failed for relative paths | *7 months ago*
Campbell Barton | `fba8bf0` | Fix for stupid typo | *1 year, 1 month ago*
Campbell Barton | `e41a177` | Change pack --exclude behavior, don't touch excluded paths at all | *1 year, 1 month ago*

***

# ~FLAMENCO


**AUTHOR** | **HASH** | **MESSAGE** | **TIME**
--- | --- | --- | ---
Francesco Siddi | `e937d0c` | Merge pull request #191 from djazo/docfix |  *8 weeks ago*
Francesco Siddi | `e7239a8` | Merge pull request #190 from djazo/fix176 |  *8 weeks ago*
Francesco Siddi | `bc558cb` | Merge pull request #189 from djazo/hotfix |  *8 weeks ago*
Arto Kitula | `ac4a05f` | Added Imagemagic to worker requirements |  *8 weeks ago*
Arto Kitula | `27ad533` | fix issue #176, adding bam binary location configuration |  *8 weeks ago*
Arto Kitula | `4d55a30` | fix filename regexp on saved_file |  *8 weeks ago*
Francesco Siddi | `29be3f7` | WIP docs about worker |  *2 months ago*
Francesco Siddi | `0b412b1` | Update Docker production images to use apache2ctl |  *3 months ago*
Francesco Siddi | `5f7b53c` | Added init info to flamenco-worker |  *4 months ago*
Eibriel | `b636cc5` | Completing instructions to run Flamenco on Docker |  *5 months ago*
Francesco Siddi | `7a1b775` | Renamed DATABASE_URI to work with readme |  *5 months ago*
Francesco Siddi | `45d54d8` | Tweaks to worker service script |  *5 months ago*
Francesco Siddi | `eb3fb42` | Worker: improved help on run.py |  *6 months ago*
Francesco Siddi | `7662cba` | Expanded Docker installation guide |  *6 months ago*
Francesco Siddi | `2d61360` | Removed mentions of Grunt, since it has been replaced with Gulp |  *6 months ago*

***

#### BLENDER MANUAL


**REV** | **DEVS** | date | time | comment
--- | --- | --- | --- | ---
