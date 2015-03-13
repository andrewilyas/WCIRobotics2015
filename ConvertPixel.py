import math
#given
y = 1
y0 = 1
f = 1
h = 1 # height of the camera from the ground in cm
Hpx = 1 # height of the sceen in pixels
x = 1 #x is location of pixel on the screen
def convert(h,Hpx, x, y, y0, f):
    R = math.sqrt( (h*h)+(y*y) )
    alpha = math.atan(h/y)
    
    a = ( ( h*y )-( y0*h ) ) / ( ( y0*y ) + h*h ) #half the height of the screen in cm
    Cpx = (2*a)/Hpx
    A = math.cos(Hpx/2 -x)
    v = h / ((f*math.sin(alpha) + Cpx*(A)))
    ym =  v*( f*math.cos(alpha)-( math.sin(alpha) * ((Hpx/2) -x) * Cpx ) )         
    return ym
ym = convert(h,Hpx,x,y,y0,f)
print ym
