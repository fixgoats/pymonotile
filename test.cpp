#include <vector>

int main (int argc, char *argv[]) {
  std::vector<double> v{1, 2, 34 , 5};
  v.shrink_to_fit();
  return 0;
}
