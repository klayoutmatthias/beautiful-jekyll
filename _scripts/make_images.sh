#!/bin/bash -e

self=$(dirname $(which $0))

files=(
  samples/basic.py
  overview/samples/transformation.py
  overview/samples/instances.py
  overview/samples/cell_global_bbox.py
  overview/samples/cell_layer_bbox.py
  overview/geometry/samples/box_intersections.py
  overview/geometry/samples/box_unions.py
  overview/geometry/samples/polygon1.py
  overview/geometry/samples/polygon2.py
  overview/geometry/samples/polygon3.py
  overview/geometry/samples/polygon4.py
  overview/geometry/samples/path1.py
  overview/geometry/samples/path2.py
  overview/geometry/samples/path3.py
  overview/geometry/samples/path4.py
  overview/geometry/samples/path5.py
  overview/geometry/samples/path6.py
  overview/geometry/samples/path7.py
  overview/geometry/samples/path8.py
  overview/geometry/samples/path_to_polygon.py
  overview/geometry/samples/text1.py
  overview/geometry/samples/text3.py
  overview/geometry/samples/region1.py
  overview/geometry/samples/region2.py
  overview/geometry/samples/region3.py
  overview/geometry/samples/region4.py
  overview/geometry/samples/region5.py
  overview/geometry/samples/region6.py
  overview/geometry/samples/region7.py
  overview/geometry/samples/region8.py
  overview/geometry/samples/region9.py
  examples/gratings_flat/gratings_flat.py
  examples/gratings_hierarchical/gratings_hierarchical.py
  examples/nuts_and_bolts/nuts_and_bolts.py
  examples/cheese/cheese.py
  examples/save_layout_options/save_layout_options.py
  examples/flatten/flatten.py
  examples/layout_merge/layout_merge.py
  examples/clip/clip.py
  examples/pcell_instances/pcell_instances.py
  examples/glyphs/glyphs.py
  examples/eggs/eggs.py
)

force=0
if [ "$1" = "-f" ]; then
  force=1
fi

for f in ${files[@]}; do

  echo "----------------------------------------------"
  echo "Running sample $f .."

  png=${f/.py/.png}

  if [ $force = 0 ] && [ -e $png ] && [ $png -nt $f ]; then

    echo "SKIP: Image file is aready up to date."

  else

    pushd $(dirname $f) >/dev/null

    ff=$(basename $f)
    if [ -e ${ff/.py/_plus.py} ]; then
      cat $ff ${ff/.py/_plus.py} | python3 
    else
      python3 $ff
    fi

    popd >/dev/null

    shopt -s nullglob

    for gds in $(dirname $f)/*.gds; do
      gds_png=${gds/.gds/.png}
      if ! [ -e $gds_png ] || [ $gds -nt $gds_png ]; then
        klayout -t -c $self/klayout.rc -rx -z -r $self/make_image.py -rd input=$gds -rd output=$gds_png
      fi
    done

  fi

done
  
