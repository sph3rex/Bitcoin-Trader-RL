from unittest import mock
from unittest.mock import MagicMock

from lib.RLTrader import RLTrader
from lib.TraderArgs import TraderArgs

class TestRLTrader():
    def setup_class(self):
        self.parser = TraderArgs().get_parser()

    @mock.patch.object(RLTrader, 'initialize_data', return_value=True)
    @mock.patch.object(RLTrader, 'optimize', return_value=True)
    @mock.patch.object(RLTrader, 'initialize_optuna', return_value=True)
    def test_that_args_get_injected_correctly(self, data_mock, opt_mock, init_mock):
        args = self.parser.parse_args(['optimize'])
        sut = RLTrader(**vars(args), logger=MagicMock())
        sut.study_name = 'test'
        with mock.patch('lib.util.logger.init_logger'):
            assert(sut.tensorboard_path == args.tensorboard_path)
            assert(sut.params_db_path == args.params_db_path)
            assert(sut.model_verbose == args.model_verbose)
            assert(sut.nminibatches == args.nminibatches)
            assert(sut.train_split_percentage == args.train_split_percentage)
            assert(sut.input_data_path == args.input_data_path)
            assert(sut.model_verbose == args.model_verbose)
            assert(sut.input_data_path == args.input_data_path)
