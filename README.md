# Prime Analysis Tools <!-- omit in toc -->
- [Quick Start - Running Application](#quick-start---running-application)
  - [Requirements](#requirements)
  - [OPTIONAL - Git Bash](#optional---git-bash)
  - [Clone The Repository](#clone-the-repository)
  - [Virtual Environment](#virtual-environment)
  - [Running Tests, and Running the App](#running-tests-and-running-the-app)
- [Developer Section](#developer-section)
  - [Directory](#directory)
    - [Directory Structure](#directory-structure)
    - [Directory Summary:](#directory-summary)
  - [Primary Tool Development <a name="Primary Tool Development"></a>](#primary-tool-development-)
<a name="quick-start---running-application"></a>
## Quick Start - Running Application ##
### Requirements ##
All that is needed to start the Quick Start Guide is Python v=3.9.1
### OPTIONAL - Git Bash
* Using Git Bash is helpful when it comes to navigating directories and running scripts from the command line
* Download here: 
	* <https://git-scm.com>
* Should already have it if Git is on your system
### Clone The Repository
* Navigate to where your project directory is, or create a new one.
* Using preferred method, clone the repsoitory
	* `git clone https://adambea@bitbucket.org/missionbio/prime.git`
### Virtual Environment
1. Download and install Anconda from
    * <https://www.anaconda.com/products/individual>
2. Navigate to the /build folder in the repository, open your choice of command prompt.
3. Enter the following command:
	* `conda env create --file environment.yml`
4. Navigate back to the root directory
5. Activate your new virtual environment with the following code
	* `conda activate prime_env`
### Running Tests, and Running the App
1. Verify installation by running the tests from the root directory with
	* `pythom -m pytest`
3. Run the application with
	* `streamlit run app.py`
## Developer Section
### Directory ###
#### Directory Structure ####
* The directory for the application is set up as follows
	* |_build
		* |_requirements.txt
		* |_build_env.yml
	* |_helper
		* |_init.py
		* |_Analyze.py
		* |_Beadcounting.py
		* |_Detection.py
		* |_Tools.py
		* |_Visualization.py
	* |_prime
		* |_init.py
		* |_Brightfield.py
		* |_Fluoresence.py
		* |_TubeVolume.py
	* |_tests
		* |_helper_tests
		* |_imgs
		* |_prime_tests
		* |_test_example.py
	* |_.gitignore
	* |_README.MD
	* |_app.py
#### Directory Summary: ####
* Build: Contains files to help build the application
    * Contains .yml file for venv creation
    * Contains requirements.txt for future build needs
* Helper: Contains files with helper functions
* Prime: Contains all the primary analysis functions: Brightfield, Fluorescence, and Tube Volume.
* Tests: Contains tests for each type of function and images needed for those tests
    * helper_Tests: Tests for helper functions
    * prime_Tests: Tests for prime functions
    * imgs: Images for prime_tests
    * test_example.py: File showing how to write a pytest
* app.py: application entry point
### Primary Tool Development <a name="Primary Tool Development"></a> ###
