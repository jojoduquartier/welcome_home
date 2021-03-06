# Copyright 2018-2019 QuantumBlack Visual Analytics Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND
# NONINFRINGEMENT. IN NO EVENT WILL THE LICENSOR OR OTHER CONTRIBUTORS
# BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# The QuantumBlack Visual Analytics Limited ("QuantumBlack") name and logo
# (either separately or in combination, "QuantumBlack Trademarks") are
# trademarks of QuantumBlack. The License does not grant you any right or
# license to the QuantumBlack Trademarks. You may not use the QuantumBlack
# Trademarks or any confusingly similar mark as a trademark for your product,
#     or use the QuantumBlack Trademarks in any other manner that might cause
# confusion in the marketplace, including but not limited to in advertising,
# on websites, or on software.
#
# See the License for the specific language governing permissions and
# limitations under the License.
"""Example code for the nodes in the example pipeline. This code is meant
just for illustrating basic Kedro features.

PLEASE DELETE THIS FILE ONCE YOU START WORKING ON YOUR OWN PROJECT!
"""

from kedro.pipeline import Pipeline, node

from .nodes import split_data, combine_train_x, combine_train_y, combine_test_x, combine_test_y


def create_split_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=split_data,
                inputs=["josiah", "params:split_ratio", "params:josiah_label", "params:random_state"],
                outputs=dict(
                    train_x="josiah_train_x",
                    train_y="josiah_train_y",
                    test_x="josiah_test_x",
                    test_y="josiah_test_y",
                ),
            ),
            node(
                func=split_data,
                inputs=["amaka", "params:split_ratio", "params:amaka_label", "params:random_state"],
                outputs=dict(
                    train_x="amaka_train_x",
                    train_y="amaka_train_y",
                    test_x="amaka_test_x",
                    test_y="amaka_test_y",
                ),
            ),
            node(
                func=split_data,
                inputs=["derrick", "params:split_ratio", "params:derrick_label", "params:random_state"],
                outputs=dict(
                    train_x="derrick_train_x",
                    train_y="derrick_train_y",
                    test_x="derrick_test_x",
                    test_y="derrick_test_y",
                ),
            ),
            node(
                func=split_data,
                inputs=["others", "params:split_ratio", "params:others_label", "params:random_state"],
                outputs=dict(
                    train_x="others_train_x",
                    train_y="others_train_y",
                    test_x="others_test_x",
                    test_y="others_test_y",
                ),
            ),
        ]
    )


def create_combine_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=combine_train_x,
                inputs=["josiah_train_x", "amaka_train_x", "derrick_train_x", "others_train_x"],
                outputs=dict(train_x="train_x")
            ),
            node(
                func=combine_train_y,
                inputs=["josiah_train_y", "amaka_train_y", "derrick_train_y", "others_train_y"],
                outputs=dict(train_y="train_y")
            ),
            node(
                func=combine_test_x,
                inputs=["josiah_test_x", "amaka_test_x", "derrick_test_x", "others_test_x"],
                outputs=dict(test_x="test_x")
            ),
            node(
                func=combine_test_y,
                inputs=["josiah_test_y", "amaka_test_y", "derrick_test_y", "others_test_y"],
                outputs=dict(test_y="test_y")
            ),
        ]
    )


def create_pipeline(**kwargs):
    return create_split_pipeline() + create_combine_pipeline()

# def create_pipeline(**kwargs):
#     return Pipeline(
#         [
#             node(
#                 split_data,
#                 ["example_iris_data", "params:example_test_data_ratio"],
#                 dict(
#                     train_x="example_train_x",
#                     train_y="example_train_y",
#                     test_x="example_test_x",
#                     test_y="example_test_y",
#                 ),
#             )
#         ]
#     )

# conda activate kwabo
# cd /Users/josiahhounyo/Documents/py_server
# python -m http.server [<portNo>]
# http://10.0.0.212:8000//welcome.mp3
# ifconfig and look for en0 - inet
