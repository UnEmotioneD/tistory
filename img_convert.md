# Convert Image

Convert images with `convert` command

## List of Contents

- [Rotate](#rotate)
- [Resize](#resize)
- [Mirror](#mirror)
- [Change Format](#change-format)
- [Adjust Quality](#adjust-quality-jpeg)
- [Strip Metadata](#strip-metadata-exif)

---

## Rotate

Rotate image clockwise:

```sh
convert foo.jpg -rotate 90 bar.jpg
```

`-rotate` option can accept any real number

---

## Resize

Resize by percentage:

```sh
convert foo.jpg -resize 50% bar.jpg
```

Resize to exact dimensions:

```sh
convert foo.jpg -resize 800x600 bar.jpg
```

Keep aspect ratio (fit within box):

```sh
convert foo.jpg -resize 800x600\> bar.jpg
```

---

## Mirror

Vertical flip:

```sh
convert foo.jpg -flip bar.jpg
```

Horizontal mirror:

```sh
convert foo.jpg -flop bar.jpg
```

---

## Change Format

Convert PNG to JPG:

```sh
convert foo.png bar.jpg
```

Batch convert:

```sh
convert *.png *.jpg
```

---

## Adjust Quality (JPEG)

Lower quality (smaller file):

```sh
convert foo.jpg -quality 85 bar.jpg
```

---

## Strip Metadata (EXIF)

```sh
convert foo.jpg -strip bar.jpg
```

---

### Happy Hacking 🎉
