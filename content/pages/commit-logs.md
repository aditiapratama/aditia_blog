title: Commit Logs

<h2 style="border-bottom: 3px solid #cfd8dc; padding-bottom:15px;">
  <i class="bf-blender"></i> BLENDER - BRANCH :
  <i style="text-transform:uppercase;color:#c7254e">master</i>
  <span style="font-size:16px;font-weight:200;float:right;"> Compiled :
    <time class="timeago" datetime="Thu, 11 Aug 2016 05:13:10 +0700">Thu, 11 Aug 2016 05:13:10 +0700</time>
  </span>
</h2>

AUTHOR | HASH | MESSAGE
--- | --- | ---
Lukas Stockner | [`7c3a06c`](https://developer.blender.org/rB7c3a06c) | Cycles Tests: Add test for correct 16 byte alignment of KernelData structs
Mai Lavelle | [`4d1bf14`](https://developer.blender.org/rB4d1bf14) | Cycles Standalone: Fix building after microdisp changes
Lukas Stockner | [`82e65ab`](https://developer.blender.org/rB82e65ab) | Cycles: Fix KernelIntegrator padding to 16-byte boundary
Bastien Montagne | [`498b7bd7`](https://developer.blender.org/rB498b7bd7) | Updated install_deps.sh to OSD 3.0.5 (and switch from git repo to download archive of sources).
Lukas Stockner | [`ef27d8e`](https://developer.blender.org/rBef27d8e) | Cycles Standalone: Add option to set the tile size from the command line
Lukas Stockner | [`bbbc079`](https://developer.blender.org/rBbbbc079) | Cycles: Correct maximum number of textures on pre-Kepler CUDA cards
Antonioya | [`ebdb549`](https://developer.blender.org/rBebdb549) | GPencil: Avoid segment fault if new stroke function is called without colorname
Antonioya | [`774beb7`](https://developer.blender.org/rB774beb7) | GPencil: Rename color name property to keep consistency in naming
Bastien Montagne | [`c19d527`](https://developer.blender.org/rBc19d527) | Fix crash in id remapping of Graph editor.
Sergey Sharybin | [`0433ae3`](https://developer.blender.org/rB0433ae3) | Cycles: Use proper property getter
Sergey Sharybin | [`0271952`](https://developer.blender.org/rB0271952) | Attempt to fix previous commit for non-c++11 builds
Lukas Tönne | [`3bbf8fb`](https://developer.blender.org/rB3bbf8fb) | Fix for isfinite breaking builds when WITH_CXX11 is enabled.
Sergey Sharybin | [`d5a0ae0`](https://developer.blender.org/rBd5a0ae0) | Fix T48916: Proxy Custom File is broken
Sergey Sharybin | [`1647d89`](https://developer.blender.org/rB1647d89) | Fix T49027: Sequence uses too much memory when rendering scene with lots of movie strips
Sergey Sharybin | [`f990518`](https://developer.blender.org/rBf990518) | CMake: Once again, don't use find_package to get hardcoded libraries
Sergey Sharybin | [`62b6706`](https://developer.blender.org/rB62b6706) | CMake: Remove hardcoded DIR_ROOT for alembic and MinGW
Sergey Sharybin | [`f0bf33f`](https://developer.blender.org/rBf0bf33f) | CMake: Use proper way to define debug/release libraries for alembic
Sergey Sharybin | [`bccaa994`](https://developer.blender.org/rBbccaa994) | CMake: Do not force set root folder for Alembic
Alexander Gavrilov | [`a7f6f90`](https://developer.blender.org/rBa7f6f90) | Cycles: avoid making NaNs in Vector Math node by normalizing zero vectors.
Thomas Dinges | [`c2a7317`](https://developer.blender.org/rBc2a7317) | CUDA: We don't support Toolkits < 7.5, update error message.