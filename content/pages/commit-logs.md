title: Commit Logs

<h2 style="border-bottom: 3px solid #cfd8dc; padding-bottom:15px;">
  <i class="bf-blender"></i> BLENDER - BRANCH :
  <i style="text-transform:uppercase;color:#c7254e">master</i>
  <span style="font-size:16px;font-weight:200;float:right;"> Compiled :
    <time class="timeago" datetime="Thu, 18 Aug 2016 05:34:47 +0700">Thu, 18 Aug 2016 05:34:47 +0700</time>
  </span>
</h2>

AUTHOR | HASH | MESSAGE
--- | --- | ---
Brecht Van Lommel | [`40b3674`](https://developer.blender.org/rB40b3674) | Code cleanup to use array.data() rather than &array[0].
Brecht Van Lommel | [`c0161a1`](https://developer.blender.org/rBc0161a1) | Fix T48913: cycles viewport render stuck in loop due to non-unique dupli ID.
Kévin Dietrich | [`11e9c5e`](https://developer.blender.org/rB11e9c5e) | Fix T49104: normal problem in imported Alembic objects
Kévin Dietrich | [`8e7bbe6`](https://developer.blender.org/rB8e7bbe6) | Alembic import: fix scene min/max time computation to take objects with transform animations into account.
Kévin Dietrich | [`294b075`](https://developer.blender.org/rB294b075) | Fix T49081: Alembic sampling times are not taking start frame into account.
Bastien Montagne | [`c783e65`](https://developer.blender.org/rBc783e65) | Fix/add some tooltips to 'Object Align' operator options.
Howard Trickey | [`e3b5aa9`](https://developer.blender.org/rBe3b5aa9) | Fix Bevel crashes T49088 and T48858.
Mai Lavelle | [`8cac980`](https://developer.blender.org/rB8cac980) | Cycles: Fix regression where smoke wouldn't show in renders
Antonioya | [`ab775b6`](https://developer.blender.org/rBab775b6) | Fix T49102: Angle option of new GP brush settings is too restricted in value
Sergey Sharybin | [`47e08ee`](https://developer.blender.org/rB47e08ee) | Fix T49086: UV Along Stroke can be set as vector input for environment texture
Sergey Sharybin | [`294eac2`](https://developer.blender.org/rB294eac2) | CMake: Move main platform checks to separate files
Bastien Montagne | [`186ee09`](https://developer.blender.org/rB186ee09) | More UI messages fixes and cleanup.
Sergey Sharybin | [`acbef39`](https://developer.blender.org/rBacbef39) | 2D stabilizer: Cover rotation tracks label with enabled flag
Sergey Sharybin | [`1fb8bbc`](https://developer.blender.org/rB1fb8bbc) | 2D stabilizer: Use exact getter instead of regular one followed with frame check
Sergey Sharybin | [`1e60535`](https://developer.blender.org/rB1e60535) | 2D stabilizer: Remove check for markers count in the track
Sergey Sharybin | [`069bc40`](https://developer.blender.org/rB069bc40) | 2D stabilizer: Remove redundant rows from the interface
Sergey Sharybin | [`83d94ef`](https://developer.blender.org/rB83d94ef) | 2D stabilizer: One more occurrence of len() in the drawing code
Sergey Sharybin | [`1c633de`](https://developer.blender.org/rB1c633de) | 2D Stabilizer: Use more consistent RNA naming for properties
Sergey Sharybin | [`de28940`](https://developer.blender.org/rBde28940) | 2D Stabilzier: Don't use len() for checking whether something is enabled or not
Antonioya | [`e392658`](https://developer.blender.org/rBe392658) | Fix T49100: Replace old tooltip for GPencil brush iterations