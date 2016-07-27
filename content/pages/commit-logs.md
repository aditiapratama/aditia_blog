title: Commit Logs

<h2 style="border-bottom: 3px solid #cfd8dc; padding-bottom:15px;">
  <i class="bf-blender"></i> BLENDER - BRANCH :
  <i style="text-transform:uppercase;color:#c7254e">master</i>
  <span style="font-size:16px;font-weight:200;float:right;"> Compiled :
    <time class="timeago" datetime="Wed, 27 Jul 2016 08:38:47 +0700">Wed, 27 Jul 2016 08:38:47 +0700</time>
  </span>
</h2>

AUTHOR | HASH | MESSAGE
--- | --- | ---
Julian Eisel | [`24b8e78`](https://developer.blender.org/rB24b8e78) | Correct UI names of ID types
Julian Eisel | [`3c59a50`](https://developer.blender.org/rB3c59a50) | More useful block name for report popup blocks
Sergey Sharybin | [`c1fd97f`](https://developer.blender.org/rBc1fd97f) | Fix T45936: invalid cycles motion blur for particle rotation and children.
Bastien Montagne | [`f3f10e4`](https://developer.blender.org/rBf3f10e4) | Fix T48813: Custom icon is not drawn on header / addons prefs panel.
Sergey Sharybin | [`f31f740`](https://developer.blender.org/rBf31f740) | Cycles: Proper fix for buffer overflow in volume intersect all
Sergey Sharybin | [`7030794`](https://developer.blender.org/rB7030794) | Cycles: Revert previous fixes to intersect_all functions
Bastien Montagne | [`b91aea6`](https://developer.blender.org/rBb91aea6) | Fix issues in ID usages checks - we are not interested in self-usages here.
Sergey Sharybin | [`01e3141`](https://developer.blender.org/rB01e3141) | Fix T48902: MCE Dopesheet does not respect Left Click select
Sergey Sharybin | [`711d3a8`](https://developer.blender.org/rB711d3a8) | Depsgraph: Use proper check whether ID is an object
Sergey Sharybin | [`40a0fa8`](https://developer.blender.org/rB40a0fa8) | Depsgraph: Use proper unsigned int bitfield for layers flags
Campbell Barton | [`eececb0`](https://developer.blender.org/rBeececb0) | Curve Drawing: use more closely spaced samples
Campbell Barton | [`4da8543`](https://developer.blender.org/rB4da8543) | Resolve undefined M_PI w/ MSVC2013
Campbell Barton | [`6e131ce`](https://developer.blender.org/rB6e131ce) | Call to python3 for stand-alone scripts
Sergey Sharybin | [`1ea410c`](https://developer.blender.org/rB1ea410c) | OpenSubdiv: Fix opensubdiv option obscuring the interface
Bastien Montagne | [`1870e16`](https://developer.blender.org/rB1870e16) | Cleanup: factorize the 'ensure local' part of datablock copy into a single BKE_id_copy_ensure_local function.
Lukas Stockner | [`d9cc3ea`](https://developer.blender.org/rBd9cc3ea) | Cycles: Fix rays parallel to the surface in the triangle refine and MultiGGX code
Lukas Stockner | [`83ae0a0`](https://developer.blender.org/rB83ae0a0) | Cycles: Calculate differentials in the Multiscattering GGX closures
Sergey Sharybin | [`988ec3c`](https://developer.blender.org/rB988ec3c) | OpenSubdiv: Support shadeless shading
Sergey Sharybin | [`c967a38`](https://developer.blender.org/rBc967a38) | OpenSubdiv: Fix missing support of flat shading in textured viewport
Sergey Sharybin | [`27db7ef`](https://developer.blender.org/rB27db7ef) | OpenSubdiv: Use proper material index