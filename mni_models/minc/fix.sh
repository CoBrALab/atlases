for file in *mnc; do
    mincreshape -normalize -unsigned -byte -image_range 0 255 \
        -valid_range 0 255 ${file} /tmp/$(basename ${file})
    mv -f /tmp/$(basename ${file}) ${file}
done
