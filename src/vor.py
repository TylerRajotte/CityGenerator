from scipy.spatial import Voronoi, voronoi_plot_2d
import random

resolution = 100
windowx = 500
windowy = 400
points = []
for x in range(resolution):
    points.append((random.randrange(0, windowx), random.randrange(0, windowy)))

vor = Voronoi(points)
print(vor.ridge_vertices)

