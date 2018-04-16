#include <iostream>
#include <ctime>
#include <cstdlib>
#include <math.h>



#define GetSize(array_enteros) (sizeof(array_enteros)/sizeof(*(array_enteros)))

using namespace std;

double pi = 3.1415926535897;


double interpola(double punto, double* x,  double* y)
{
  double L = 0.0; 

  int N = 10;

  for(int j=0; j < N; j++)
    {
      double producto = 1.0;
      

      for(int i=0; i < N; i++)
	{
	  
	  if(i != j)
	    {
	      producto = producto * (punto - x[i])/(x[j] - x[i]);
	    }
	}
	  
	  L = L + y[j]*producto;
    }


  return L;
}


double* fourier_img(double* y, int N)
{

  double* img = new double[N];

  for (int k=0; k < N; k++)
    {

      img[k] = 0.0;

      for (int n=0; n < N; n++)
	{
	  double w = 2.0*pi;

	  img[k] = img[k] + y[n]*sin(-w*k*n/N);
	}

      img[k] = img[k]/N;
    }

  return img;
}

double* fourier_real(double* y, int N)
{

  double* real = new double[N];


  for (int k=0; k < N; k++)
    {
      real[k] = 0.0;

      for (int n=0; n < N; n++)
	{
	  double w = 2.0*pi;

	  real[k]= real[k] + y[n]*cos(-w*k*n/N);
	}

      real[k] = real[k]/N;

    }

  return real;

}
  
  

int main( char* argc[], int argv)
{
  //ifstream arch("hola.txt");

  double* a = new double[20];

  double* b = new double[20];

  int N = 20;
  

  for (int i = 0; i < 20; i++)
    {
      a[i] = double(i*1.0);

      b[i] = pow(i, 2.0);

      cout << *fourier_real(b, N) << " " << *fourier_img(b, N) << endl;

    }




  //cout << *a << N << sizeof(*a) << sizeof(a[4]) << endl;

  //cout << interpola(2.5, a, b) << endl;

  //cout << *a << endl;

  //cout << *b << endl;

  

  


  return 0;
}
