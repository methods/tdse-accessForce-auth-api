# tdse-accessForce-auth-stub
Authorisation stub for Bids API project

## Prerequisites

- Python 3.x
- Flask
- Homebrew

## Running the API

1. Clone the repository to your local machine (RECOMMENDED: in the same directory as tdse-accessForce-bids-api):

      ```bash
      git clone
      ```
2. Navigate to the root directory of the project:

      ```bash
      cd tdse-accessForce-auth-stub
      ```
3. Install python 3.x if not already installed. You can check if it is installed by running the following command:

      ```bash
      python3 --version
      ```
4. Install Makefile if not already installed. You can check if it is installed by running the following command:

      ```bash
      make --version
      ```
5. Version 3.81 or higher is required. If you do not have Make installed, you can install it with Homebrew:

      ```bash
      brew install make
      ```
6. Run the following command to have all the commands to use the API with Makefile:

      ```bash
      gmake help
      ```
7. Run the following command to start the API:

      ```bash
      gmake run
      ```
PLEASE NOTE: This is a stub authorisation server. For full instructions on how to interact with this app, you should follow the documentation for the [Bids API](https://github.com/methods/tdse-accessForce-bids-api).