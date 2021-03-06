
import ConfigParser

#add more config params as you discover them
class Config:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path

        configParser = ConfigParser.RawConfigParser()
        configParser.read(config_file_path)
        
        #movie lens 100k dataset, 80 - 20 train/test ratio, present in data directory
        self.training_file = float(configParser.get('Config', 'rating_threshold_af'))
        self.testing_file = float(configParser.get('Config', 'rating_threshold_af'))
        
        self.small_grp_size = float(configParser.get('Config', 'rating_threshold_af'))
        self.medium_grp_size = float(configParser.get('Config', 'rating_threshold_af'))
        self.large_grp_size = float(configParser.get('Config', 'rating_threshold_af'))
        
        self.max_iterations_mf = float(configParser.get('Config', 'rating_threshold_af'))
        self.lambda_mf = float(configParser.get('Config', 'rating_threshold_af'))
        
        #AF (after factorization)
        self.rating_threshold_af = float(configParser.get('Config', 'rating_threshold_af'))
        self.num_factors_af = float(configParser.get('Config', 'rating_threshold_af'))
        self.num_recos_af = float(configParser.get('Config', 'rating_threshold_af'))
        
        #BF (before factorization)
        self.rating_threshold_bf = float(configParser.get('Config', 'rating_threshold_bf'))
        self.num_factors_bf = float(configParser.get('Config', 'rating_threshold_bf'))
        self.num_recos_bf = float(configParser.get('Config', 'rating_threshold_af'))
        
        #WBF (weighted before factorization)
        self.rating_threshold_af = float(configParser.get('Config', 'rating_threshold_wbf'))
        self.num_factors_wbf = float(configParser.get('Config', 'rating_threshold_wbf'))
        self.num_recos_wbf = float(configParser.get('Config', 'rating_threshold_af'))
        
        
        
        
        