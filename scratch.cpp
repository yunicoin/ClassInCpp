#include <iostream>
using namespace std;

class Vector
{
    double x, y;
public:
    Vector(double x, double y);
    Vector();
    double get_x() {return x;}
    double  get_y() {return y;}
    Vector operator+(Vector);
    Vector operator-(Vector);
    Vector operator*(double);
    Vector operator/(double);
    Vector operator*(Vector);
    Vector operator**(Vector);
    Vector operator<(Vector);
    Vector operator==(Vector);
    Vector operator!=(Vector);
    Vector operator|();
    friend ostream& operator<<(ostream&, const Vector&);
}
Vector::Vector(double k, double l)
{
    x=k;
    y=l;
}
Vector::Vector()
{
    x=0;
    y=0;
}
Vector Vector::operator+(Vector a)
{
    return Vector(x+a.x, y+a.y);
}
Vector Vector::operator-(Vector a)
{
    return Vector(x-a.x, y-a.y);
}
Vector Vector::operator*(Vector a)
{
    return double (x*a.x+y*a.y);
}
Vector Vector::operator**(Vector a)
{
return double (x*y.a-y*x.a);
}
Vector Vector::operator==(Vector a)
{
    if x==a.x and y==a.y{
        return 1;
    }
    else
    {
        return 0;
    }
}
Vector Vector::operator!=(Vector a)
{
    if x==a.x and y==a.y{
        return 0;
    }
    else
    {
        return 1;
    }
}
Vector Vector::operator*(double a) {
    return Vector(x*a,y*a);
}
Vector Vector::operator/(double a) {
    return Vector(x/a,y/a);
}
Vector Vector::operator|()
{
    return double (x*x+y*y);
}
int main()
{
    double a, b;
    cin>> a >> b;
    Vector z(a, b);
    cout<<z;
}