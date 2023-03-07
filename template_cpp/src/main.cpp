#include "test.hpp"

int main()
{
    Greet();

    Eigen::Matrix<double, 10, 10> A;
    Eigen::Matrix<double, 10, 10> B;
    A.setRandom();
    B.setRandom();
    A(9, 0) = 1.234;
    B(9, 0) = 0;
    cout << A*B << endl;

    return 0;
}