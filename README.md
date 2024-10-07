# WasteX: Landfill Selection Optimization

WasteX is a Python-based tool developed to solve optimization problems related to landfill selection. The program utilizes Dijkstra's algorithm (Dijkstra, 1959) to determine the 3 optimal landfills for waste collection based on the distances traveled from 9 towns. The tool aims to minimize the distances traveled by waste collection trucks while enabling a maximum of 3 landfills. The program takes into account various factors, such as waste density and growth rate. This project features a graphical interface developed using the Tkinter library to visualize and optimize the selection of landfills.

## Features

-Optimized Landfill Selection: Efficient identification of the best landfills to minimize transportation distances.

-Minimization of Travel Distance: Reduces the total kilometers traveled by waste collection trucks.

-Consideration of Waste Density and Growth Rate: Factors in waste density and growth rate to ensure efficient waste management.

-Maximum Number of Enabled Landfills: Restricts the number of active landfills to a maximum of 3.

-Visualization of maps with geographic coordinates.

-Interactive interface with buttons to control the behavior of the legend and visualized objects.

-Two maps available for result visualization.

## Requirements

Python version 3 or above, the `pandas` library for data manipulation and reading from CSV files, the `openpyxl` library required for reading Excel files, and the  `pulp` library for solving linear programming problems. You can install them using:

```bash
pip install pandas
```

```bash
pip install openpyxl
```

```bash
pip install pulp
```

## Files

`Toneladas y Distancia.csv`: CSV file containing the distances between towns and landfills in the sheet `Distancia Municipios a Rellenos`.

`main.py`: The main file that runs the graphical interface.

`algoritmo_distancias.py`: Contains the algorithm that calculates the optimal distances for selecting the landfills. Output: A tuple with the numbers corresponding to the three optimal landfills.

`Longitudes_Tabla.xlsx`: Excel file containing geographic coordinates in degrees, minutes, and seconds format.

`conversion_grados.py`: Functions that convert geographic coordinates. Output: A list with the coordinates converted to decimal degrees, along with the calculated relative distances.

## Usage
Place the `Toneladas y Distancia.xlsx` file in the same directory as the Python script.

The function `fun_algoritmo()` performs the following tasks:

-Reads the CSV file and extracts the Distancia Municipios a Rellenos data.

-Sums the distances from towns to each landfill.

-Sorts the landfills based on total distance.

-Returns the three landfills with the lowest total distance.

-Coordinate Conversion and Distance Calculation


This project also includes a Python function that converts geographic coordinates from degrees, minutes, and seconds to decimal degrees and calculates relative distances in latitude and longitude between a series of points and a reference coordinate.

## Interface Structure

The graphical interface consists of a Canvas displaying the base map with the geographic coordinates of the potential landfills. Buttons in the legend allow interaction with the points on the map, changing their colors based on their status. A "Calculate Optimal Location" button executes the algorithm to highlight the best landfills.

## Functionality

-Geographic Coordinate Conversion: Converts geographic coordinates from degrees, minutes, and seconds format to decimal degrees.

-Relative Distance Calculation: Computes relative distances in latitude and longitude between coordinates of points of interest and a predefined reference point.

-Coordinate Data Utilization: The program uses coordinate data stored in a CSV file for easy input and manipulation.


## Structure of the Code

The program utilizes the following key functions:

`fun_algoritmo()`: Returns the best landfill locations based on minimizing distances.

`grados_fun()`: Converts geographic coordinates to a format suitable for visualization on maps.

`minim_fun()`: Calculates optimal locations using the algorithm and updates the map accordingly.

## Conclusion

WasteX provides an efficient solution for optimizing landfill selection and waste management through distance calculations and Dijkstra's algorithm, making it a valuable tool for urban planning and environmental management.

## 🔗 .exe file

[.exe file](https://drive.google.com/drive/folders/1oftxZcIyBHwX0wMPNntaELyZPbKcVTWt?usp=sharing)

## 🔗 Contacts

-Flores Castillo Miriam del Carmen: https://www.linkedin.com/in/mirflores/

-García Fernández Irving Fernando: https://www.linkedin.com/in/irving-fernando-garc%C3%ADa-fern%C3%A1ndez-03369b316/

-Guijarro Toto Azucena: https://www.linkedin.com/in/azucena-guijarro-toto-121665331/

-Hernández Lozano Victoria Guadalupe: victoriahernandezloza2a@gmail.com

-Martínez Córdoba Luis Roberto: https://www.linkedin.com/in/luis-roberto-mart%C3%ADnez-c%C3%B3rdoba-06b97a271/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app

-Morlet Avilés Gustavo Alejandro: https://www.linkedin.com/in/gustavo-alejandro-morlet-avil%C3%A9s-63023b1ab/
