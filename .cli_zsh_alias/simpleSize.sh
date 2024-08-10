# Add `source [full path to script]/simpleSize.sh` to ~/.bashrc or ~/.zshrc
# to load this function into your shell session

simplesize() {

	# Get the directory of the current script
	# NOTE: Change the following line to where the virtual environment is located
    local root_path="/Users/ethan/projects/mac_related/"
    local venv="venv"
    local source_folder="simpleSize/"
    local driver_script="list_contents.py"

    # Get the directory from which the user is calling this script
	local calling_dir=$(pwd)

    # If the virtual environment does not exist, end the script
    if [ ! -d "$root_path$venv" ]; then
        echo "Error: Virtual environment '$venv' does not exist."
        return 1
    fi

    # Activate the virtual environment
    source "$root_path$venv"/bin/activate

    # Run the Python script with the passed arguments
    if [ -f "$root_path$source_folder$driver_script" ]; then
        python3 "$root_path$source_folder$driver_script" "$@"
    else
        echo "Error: $driver_script not found in the current directory."
    fi

    # Deactivate the virtual environment
    deactivate
}
