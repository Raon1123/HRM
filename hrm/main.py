def main():
    print("Hello from hrm!")


def build_sudoku():
    """Build Sudoku dataset with specific configuration."""
    import sys
    import os
    # Add project root and dataset directory to path
    project_root = os.path.dirname(os.path.dirname(__file__))
    dataset_dir = os.path.join(project_root, 'dataset')
    sys.path.insert(0, project_root)
    sys.path.insert(0, dataset_dir)
    
    from build_sudoku_dataset import DataProcessConfig, preprocess_data
    
    # Create config with specific parameters
    config = DataProcessConfig(
        output_dir="data/sudoku-extreme-1k-aug-1000",
        subsample_size=1000,
        num_aug=1000
    )
    
    # Run the preprocessing
    preprocess_data(config)


def train_sudoku():
    """Train Sudoku model with specific configuration."""
    import sys
    import os
    from hydra import compose, initialize_config_dir
    
    # Set environment variable
    os.environ['OMP_NUM_THREADS'] = '8'
    
    # Change to project root directory for Hydra config path resolution
    project_root = os.path.dirname(os.path.dirname(__file__))
    os.chdir(project_root)
    
    # Add project root to path
    sys.path.insert(0, project_root)
    
    # Compose Hydra config programmatically
    overrides = [
        'data_path=data/sudoku-extreme-1k-aug-1000',
        'epochs=20000',
        'eval_interval=2000',
        'global_batch_size=384',
        'lr=7e-5',
        'puzzle_emb_lr=7e-5',
        'weight_decay=1.0',
        'puzzle_emb_weight_decay=1.0'
    ]
    
    config_dir = os.path.join(project_root, "config")
    with initialize_config_dir(config_dir=config_dir, version_base=None):
        hydra_config = compose(config_name="cfg_pretrain", overrides=overrides)
    
    # Import and call the launch function with composed config
    import pretrain
    pretrain.launch(hydra_config)


if __name__ == "__main__":
    main()
