# Dense Image Matching

## Stero Problem

If cameras are aligned vertically, then pixels are only shifted horizontally in the two images. 

Use a scanline (horizontal line) to compare pixel values and pick the pixel with minimum match cost. 
- This leaves too much ambiguity - a lot of pixels have very similar values.
- Improvement is to use windows instead of individual pixels

## Window based matching

Slide a window across the scanline and find the minimum value using sum of absolute differences (SAD). 

Problems include
- Not knowing what **window size** to use.
- **Repeating patterns** on the scanline confusing the window.
- **Textureless** regions are difficult.
- **Occlusions** as a result of perspective change

## Detecting Occlusion

