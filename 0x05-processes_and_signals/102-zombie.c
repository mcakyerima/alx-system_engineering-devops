#include <unistd.h> /* For sleep */
#include <stdlib.h> /* For exit */
#include <stdio.h> /* For printf */

/**
 * infinite_while - Creates an infinite sleep loop.
 *
 * This function creates an infinite loop using the sleep function.
 *
 * Return: Always returns 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates 5 zombie processes.
 *
 * This function creates 5 zombie processes by forking child processes.
 *
 * Return: Returns the result of the infinite_while function (should never return).
 */
int main(void)
{
	pid_t child_pid;
	unsigned int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", child_pid);
	}
	return (infinite_while());
}
