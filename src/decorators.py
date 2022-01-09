import functools
import logging
import os

import dill


def repeat(num_times):
    """
    Decorator for calling a function multiple times.
    :param num_times: number of repeated calls
    :return: array of results
    """
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logging.debug(f'Running function {num_times} times')

            results = []
            for i in range(num_times):
                logging.debug(f'Executing {i+1} run')
                results.append(func(*args, **kwargs))
            return results

        return wrapper

    return decorator_repeat


def get_from_cache_or_run(cache_path):
    """
    If a file exists at certain path it is loaded, otherwise the function is run
    :param cache_path: path to cache file
    :return: cached file or recomputed output
    """

    def decorator_cache(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            os.makedirs(os.path.dirname(cache_path), exist_ok=True)

            if os.path.exists(cache_path):
                logging.debug(f'Loading cache from file {cache_path}')
                with open(cache_path, 'rb') as f:
                    return dill.load(f)
            else:
                logging.debug(f'Recomputing function and saving the output to {cache_path}')
                res = func(*args, **kwargs)
                with open(cache_path, 'wb') as f:
                    dill.dump(res, f)

                return res

        return wrapper

    return decorator_cache
