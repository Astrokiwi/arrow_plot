def arrow_plot(ax,x,y,color='blue',quiver_thickness=0.005,edgecolor=None,facecolor=None,marker='o'):
    """arrow_plot
    
    Plots a series of points connected by arrows at the half-way point.
    
    Oddly, `plot` uses a different scale for `linewidth` than `quiver` does for `width`, so this just uses `quiver` twice - once
    for the ``background'' lines, and once to place arrows in the middle. Thickness and color are set with kwargs.
    
    You can plot this on an axis/subplot, or you can pass `matplotlib.pyplot` or whatever and it'll work too
    """
    if edgecolor is None:
        edgecolor=color
    if facecolor is None:
        facecolor=color
    dx = x[1:]-x[:-1]
    dy = y[1:]-y[:-1]
    ax.quiver(x[:-1],y[:-1],dx,dy,
                scale=1,scale_units='xy',angles='xy',
                headwidth=0.,headlength=0.,headaxislength=0.,
                width=quiver_thickness,color=color)
    ax.quiver(x[:-1],y[:-1],dx/2,dy/2,
                scale=1,scale_units='xy',angles='xy',
                width=quiver_thickness,color=color)
    ax.scatter(x,y,marker=marker,edgecolor=color,facecolor=color)
    
