#include <windows.h>

int main(){
    MessageBoxA(
        NULL,
        "I AM INSIDE A CAVE!!!",
        "ERROR",
        MB_OK | MB_ICONERROR
    );

    return 0;
}