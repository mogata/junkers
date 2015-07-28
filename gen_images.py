#!/usr/bin/env python

import Image
import sys
import os
import random

# Globals

ASSETDIR="assets/backgrounds/"

# mkdir asset_library

if not os.path.exists( ASSETDIR ):
  os.makedirs( ASSETDIR )

random.seed()

for i in range(30):
  r = random.randrange(255)
  g = random.randrange(255)
  b = random.randrange(255)

  img = Image.new( "RGB", ( 32, 32), "rgb(%d,%d,%d)" % ( r,g,b ) )
  img.save( "%s%s.png" % ( ASSETDIR, i ), "png" )
