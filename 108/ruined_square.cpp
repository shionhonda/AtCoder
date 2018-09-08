#include<iostream>
using namespace std;

struct Vec {
  int x;
  int y;
};

Vec add(Vec v1, Vec v2) {
  Vec u;
  u.x = v1.x + v2.x;
  u.y = v1.y + v2.y;
  return u;
}

Vec subtract(Vec v1, Vec v2) {
  Vec u;
  u.x = v1.x - v2.x;
  u.y = v1.y - v2.y;
  return u;
}

Vec rotate(Vec p1, Vec p2) {
  Vec u, v;
  u = subtract(p2, p1);
  v.x = -u.y;
  v.y = u.x;
  return v;
}

int main() {
  Vec p1, p2, p3, p4;
  cin >> p1.x >> p1.y >> p2.x >> p2.y;
  Vec v = rotate(p1, p2);
  p3 = add(p2, v);
  p4 = add(p1, v);
  cout << p3.x << " " << p3.y << " ";
  cout << p4.x << " " << p4.y << endl;
  return 0;
}
