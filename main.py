from rgbmatrix import RGBMatrix, RGBMatrixOptions
from constants import SCRIPT_NAME, SCRIPT_VERSION
from utils import args, led_matrix_options
from renderer.main import MainRenderer
from renderer.loading import Loading
from data.config import Config
from data.data import Data

# Get CLI arguments
args = args()

# Check for LED configuration arguments
matrixOptions = led_matrix_options(args)

# Initialize the matrix
matrix = RGBMatrix(options=matrixOptions)

# Print script details on startup
print(f"{SCRIPT_NAME} - {SCRIPT_VERSION} ({matrix.width}x{matrix.height})")

# Read scoreboard options from config.json if it exists
config = Config(matrix.width, matrix.height)

# Display loading screen
Loading(matrix, config).render()

# Fetch initial data
data = Data(config)

MainRenderer(matrix, data).render()