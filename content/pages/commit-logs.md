title: Commit Logs

<h2 style="border-bottom: 3px solid #cfd8dc; padding-bottom:15px;">
  <i class="bf-blender"></i> BLENDER - BRANCH :
  <i style="text-transform:uppercase;color:#c7254e">master</i>
  <span style="font-size:16px;font-weight:200;float:right;"> Compiled :
    <time class="timeago" datetime="Sat, 20 Aug 2016 05:12:23 +0700">Sat, 20 Aug 2016 05:12:23 +0700</time>
  </span>
</h2>

AUTHOR | HASH | MESSAGE
--- | --- | ---
Brecht Van Lommel | [`cf53389`](https://developer.blender.org/rBcf53389) | Fix T49090: color picking draws wrong when using subsurf in material draw mode.
Bastien Montagne | [`62e3849`](https://developer.blender.org/rB62e3849) | Fix T49105: Array modifier displayed in Edit mode crashes on selection, with End Cap enabled.
Bastien Montagne | [`33fbf9b`](https://developer.blender.org/rB33fbf9b) | Fix broken keymap loading with disabled ndof - revert part of recent rBb10d0058d72da30
Sergey Sharybin | [`793900d`](https://developer.blender.org/rB793900d) | 2D stabilization: Make interface more compact
Kévin Dietrich | [`5f7611a`](https://developer.blender.org/rB5f7611a) | Alembic: fix crash accessing invalid objects.
Kévin Dietrich | [`bf48750`](https://developer.blender.org/rBbf48750) | Fix T49111: Automatically add file path suffix for Alembic and Collada export.
Julian Eisel | [`4d8ac1e`](https://developer.blender.org/rB4d8ac1e) | Cleanup: Remove redundant comment
Sergey Sharybin | [`ca5271e`](https://developer.blender.org/rBca5271e) | Cycles: Fix wrong allocator used for spatial builder
Bastien Montagne | [`f4e4009`](https://developer.blender.org/rBf4e4009) | Cleanup: some bad sizeof() usages.
Bastien Montagne | [`2e6d427`](https://developer.blender.org/rB2e6d427) | Cleanup/security fix: do not use strcpy (at least in new code).
Bastien Montagne | [`7b4ba65`](https://developer.blender.org/rB7b4ba65) | Cleanup for previous commit (nasty IDE replacing tads with spaces, tsst)
Bastien Montagne | [`b4d36c7`](https://developer.blender.org/rBb4d36c7) | Two fixes for optional ndof & fix bplayer for that...
Bastien Montagne | [`7b78532`](https://developer.blender.org/rB7b78532) | Freestyle: fix wrong arg order, and cleanup confusing loop (both reported by coverity).
Bastien Montagne | [`26f4f7e`](https://developer.blender.org/rB26f4f7e) | Final UI messages fixes (for this session...).
Thomas Beck | [`8a72ec8`](https://developer.blender.org/rB8a72ec8) | Fix bplayer (c) after NDOF changes from merwin
Sergey Sharybin | [`12c3002`](https://developer.blender.org/rB12c3002) | Cleanup: ifdef function which is only used from ifdef-ed code
Mike Erwin | [`b10d005`](https://developer.blender.org/rBb10d005) | NDOF: compile 3D mouse code only if WITH_INPUT_NDOF
Mike Erwin | [`a195dd1`](https://developer.blender.org/rBa195dd1) | NDOF: suppress buttons debug log
Brecht Van Lommel | [`f92a6b8`](https://developer.blender.org/rBf92a6b8) | Fix compiler warning after fix for T48913.
Brecht Van Lommel | [`e8b5e66`](https://developer.blender.org/rBe8b5e66) | Code cleanup to use array.data() rather than &array[0]