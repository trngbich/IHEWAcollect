import os
import inspect

import IHEWAcollect


def main():
    path = os.path.join(
        os.getcwd(),
        os.path.dirname(
            inspect.getfile(
                inspect.currentframe()))
    )

    product = 'GPM'
    version = 'v6'
    parameter = 'precipitation'
    resolution = 'monthly'
    variable = 'PCP'
    bbox = {
        'w': -19.0,
        'n': 38.0,
        'e': 55.0,
        's': -35.0
    }
    period = {
        's': '2008-01-01',
        'e': '2008-01-02'
    }
    nodata = -9999

    download = IHEWAcollect.Download(workspace=path,
                                     product=product,
                                     version=version,
                                     parameter=parameter,
                                     resolution=resolution,
                                     variable=variable,
                                     bbox=bbox,
                                     period=period,
                                     nodata=nodata,
                                     is_status=False)


if __name__ == "__main__":
    main()