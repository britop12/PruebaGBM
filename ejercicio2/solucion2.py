def findChampions(input_lines):
    input_lines = input_lines.strip().split("\n")
    idx = 0
    output = []

    while idx < len(input_lines):
        # Get G and P
        G, P = map(int, input_lines[idx].split())
        if G == 0 and P == 0:
            break
        idx += 1

        # Collect results of the races
        race_results = []
        for i in range(G):
            race_results.append(list(map(int, input_lines[idx].split())))
            idx += 1
        # print(race_results)
            
        # Get S (number of scoring systems)
        S = int(input_lines[idx])
        idx += 1

        # Collect scoring systems    
        for score_system in range(S):
            # Get K and system_points
            system_info = list(map(int, input_lines[idx].split()))
            K, system_points = system_info[0], system_info[1:]

            # Initialize scores for each pilot
            scores = [0] * P

            # Update scores based on the current scoring system
            for race in race_results:
                for pilot, position in enumerate(race):
                    # print(pilot+1, position)
                    # Check if the place is within the points allocation of the system
                    if position <= K:
                        scores[pilot] += system_points[position - 1]
            # print(scores)
                        
            # Identify the highest score
            highest_score = max(scores)

            # Check if there are multiple pilots with the highest score
            b = scores.count(highest_score)
            if b > 1:
                champions = []
                for i in range(len(scores)):
                    if scores[i] == highest_score:
                        champions.append(str(i + 1))
            else:
                champions = [str(scores.index(highest_score) + 1)]

            output.append(" ".join(champions))
            idx += 1

    return "\n".join(output)

if __name__ == "__main__":
    input_lines = ""

    G, P = map(int, input("Ingresa G y P: \n").split())
    input_lines += f"{G} {P}\n"

    for i in range(G):
        input_lines += input(f"Ingresa los resultados de la carrera {i+1}: \n") + "\n"

    S = int(input("Ingresa S: \n"))
    input_lines += f"{S}\n"

    for i in range(S):
        input_lines += input(f"Ingresa K y los puntos del sistema {i+1}: \n") + "\n"
    print("Output:")
    print(findChampions(input_lines))
