# arrow_plot
A simple function to plot a series of points connected by arrows in matplotlib

Uses the `scatter` and `quiver` functions to draw a series of markers, connected them with lines, and place arrows half-way along each line. To use:

```arrow_plot(ax,x,y,color='blue',quiver_thickness=0.005,edgecolor=blue,facecolor=blue,marker='o')```

The kwargs are of course optional. `ax` can be a matplotlib subplot, or the `matplotlib.pyplot` object. `x` and `y` are the coordinates of the points, in order.

`matplotlib` uses a different scaling for `quiver` arrows than for `plot` lines, so the thicknesses won't be consistent with a `plot` of the same `linewidth`.
