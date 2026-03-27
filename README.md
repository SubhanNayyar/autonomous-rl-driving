# Autonomous Navigation via Double Deep Q-Networks (DDQN)
### Reinforcement Learning Project | B.S. Artificial Intelligence

This project demonstrates the application of Deep Reinforcement Learning (DRL) to train an autonomous vehicle to navigate a complex track without collision.

## 🚀 Concept: Self-Learning Agents
The agent (car) starts with zero knowledge of the track. Through a process of rewards (for distance traveled) and penalties (for collisions), the DDQN algorithm optimizes the driving policy over multiple iterations (episodes).

## 📡 Sensor Fusion: Ray-Casting
The vehicle "sees" the environment through simulated **Ray-casting Sensors**. 
* **Input:** 5 to 7 proximity "rays" measuring the distance to track boundaries.
* **POV:** These imaginary lines provide the spatial awareness needed for the agent to calculate steering angles in real-time.

## 🛠️ Technical Stack
* **Algorithm:** Double Deep Q-Network (DDQN) to reduce overestimation bias.
* **Framework:** PyTorch / TensorFlow (Neural Network backend).
* **Environment:** Custom Python-based track simulation.
* **Optimization:** Experience Replay & Target Network updates.

## 📊 Training Results
* **Early Phase:** Random movement with frequent collisions.
* **Late Phase:** Successful lap completion as the agent learns to prioritize the "center-line" path based on proximity sensor feedback.
