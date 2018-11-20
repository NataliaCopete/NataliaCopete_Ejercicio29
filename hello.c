#include <stdio.h>
#include <omp.h>


int main(int argc, char ** argv){
    
#pragma omp parallel
{
int th_id= omp_get_thread_num();
int th_count=omp_get_num_threads();
printf("Hello from thread number:%d out of: %d\n", th_id,th_count);      
}
return 0;    
    
    
}




