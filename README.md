# 🦅 Flocking Simulation

***

![Banner](docs/banner.png)

***

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

***

## 📜 About

This project is a visual simulation of [Craig Reynolds'](https://www.red3d.com/cwr/index.html) original paper on [boids](https://www.red3d.com/cwr/boids/). The simulation demonstrates the flocking behavior of birds by simulating the interactions between individual agents. The agents follow three simple rules: alignment, cohesion, and separation. The simulation is implemented in Python using the Pygame library for visualization.

![demo](docs/demo.gif)

## 🚀 Features

- **Flocking Simulation**: Simulate the flocking behavior of birds using the boids algorithm
- **Customization**: Adjust the number of boids, speed, and other parameters to customize the simulation
- **Visualization**: Watch the boids interact on screen and observe their flocking behavior
- **Environment Variables**: Use environment variables to configure the simulation
- **Debug Mode**: Enable debug mode to visualize the vectors for alignment

![debug](docs/debug_mode.png)

## 🛠️ Installation

1. Ensure you have Python 3.11+ installed on your system.
2. Clone this repository:
   ```
   git clone https://github.com/johandielangman/flocking.git
   ```
3. Navigate to the project directory:
   ```
   cd flocking
   ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run the simulation (see [Usage](#-usage) for instructions).

## 🎮 Usage

To run the simulation:

1. Navigate to the project directory in your terminal.
2. Run the main script:
   ```
   python main.py
   ```
3. Watch as the boids flock together on the screen.
4. Close the window to end the simulation.

## ⚙️ Configuration

You can modify the following parameters in [constants.py](constants.py) to customize the simulation:

- `NUM_BOIDS`: The number of boids in the simulation
- `MAX_BOID_SPEED`: The maximum speed of the boids
- `MIN_BOID_SPEED`: The minimum speed of the boids
- `MAX_BOID_ACCELERATION`: The maximum acceleration of the boids (also known as the maximum force since each boid has a mass of 1)
- `PERCEPTION_RADIUS`: The radius within which boids perceive other boids
- `SAC_WEIGHTS`: A tuple of floats representing the weights for separation, alignment, and cohesion


## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/Johandielangman/RPS-simulation/issues) if you want to contribute.

## 📝 License

This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.

## 🙏 Acknowledgements

- [Craig Reynolds](https://www.red3d.com/cwr/index.html) for his original paper on boids
- [The Coding Train](https://www.youtube.com/watch?v=mhjuuHl6qHM&t=2227s) for the inspiration and guidance on implementing the boids algorithm

---

Made with ❤️ by Johandielangman

[![BuyMeACoffee](https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/johanlangman)