# context-state-pattern
for Raspberry Pi Controller with State Design Pattern.

## Overview
The implementation of the State Design Pattern in this project is based on the example provided at [Refactoring Guru](https://refactoring.guru/design-patterns/state/python/example).
This repository contains a controller application for Raspberry Pi, structured around the State design pattern to efficiently manage different operational states. Designed to address various concerns, the application is divided into multiple services, each maintaining its own context and capable of transitioning through multiple states. This setup is ideal for managing complex control logic in a modular and scalable way.

## Features
- **Modular Architecture**: Each service operates within its own context, improving maintainability and scalability.
- **State Design Pattern**: Utilizes the State design pattern to handle varying states within each service context.
- **Docker Integration**: Development and testing are facilitated through Docker, ensuring a smooth workflow and easy setup.
- **Graceful Shutdown**: Proper handling of termination signals to ensure graceful shutdown processes.

## Getting Started

### Prerequisites
- Docker
- Raspberry Pi (for deployment)

### Using Docker for Development
Follow these steps to set up your development environment:

1. **Clone the Repository**
   ```sh
   git clone git@github.com:kochul2000/context-state-pattern.git
   ```
2. **Navigate to the Project Directory**
   ```sh
    cd context-state-pattern
   ```
1. **Build & Run the Docker Container**
   ```sh
   docker compose up
   ```

### Acknowledgements
* Raspberry Pi Foundation
* Docker Community
