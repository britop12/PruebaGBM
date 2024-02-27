### Ejercicio 2

**Input**

The input contains several test cases. The first line of a test case contains two integers G and P separated by a blank space, indicating the number of Grand Prix (1 ≤ G ≤ 100) and the number of pilots (1 ≤ P ≤ 100).. Pilots are identified by integers from 1 to P. Each of the following G lines indicates the result of a race, and contains Q integers separated by spaces. On each line, the (i)-th number indicates the order of arrival of pilot i in the race (the first number indicates the order of arrival of a pilot 1 in that race, the second number indicates the order of arrival of pilot 2 in that race and so on). The next line contains a single integer S indicating the number of scoring systems (1 ≤ S ≤ 10), After that, each of the following lines S contains a description of a scoring system. The description of a scoring system begins with an integerK (1 ≤ K ≤ P), indicating the last finishing order to receive points, followed by a blank space, followed by e K integers k0, k1, ... , kn−1 (1 ≤ ki ≤ 100) separated by spaces, indicating the number of points to be assigned (the first integer indicates the points for first place, the second integer indicates the points for second place and so on). The last test case is followed by a line containing only two zeros separated by a blank space.

**Output**

For each scoring system in the input your program must print one line, containing the identifier of the World Champion. If more than one pilot are World Champions (ie, if there is a tie), the line must contain all World Champions, in increasing order of identifier, separated by a space.
