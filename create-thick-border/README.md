# Create a thick border around an image

If you're doing it manually, the best way to do it, is to create a rectangle and cut a hole in it:

- duplicate the image frame
- convert it to a polygon
- fill the polygon with black
- duplicate the polygon
- in the properties palette > shape > edit: shrink by 3 mm
- select both shapes
- item > path  tools > path operations -> subtract the first shape from the second
- you can put the resulting shape in the scrapbook.

If you have to do it for many images, that's not really practical.

Since the path operations are not exposed to the scripter, we have to take a different approach:

- get the frame's size
- create four rectangles at its boundary.
