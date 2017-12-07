__author__ = 'Mark Baker  email: mark2182@mac.com'

import metar_tools as metar_tools


class StationData:
    """Manages ICAO station data. Uses a dictionary to store info"""
    def __init__(self):

        self.metar = None
        self.metar_time = None
        self.taf = None
        self.taf_time = None
        self.taf_cnl = False
        self.taf_status = 0
        self.station_dict = {'ICAO': '', 'METAR_TIME': '', 'METAR': '',
                             'PREV_COLOUR': 0, 'LATEST_COLOUR': 0,
                             'TAF_TIME': '', 'TAF': '', 'TAF_MIN_COLOUR': 0,
                             'TAF_STATUS': 2, 'NEW_METAR': True}

    def update_icao_data(self, icao, metar_time, new_metar, taf_time,
                         new_taf, icao_dict):
        """Method to update station dictionary with new report info.
         icao_dict represents the previous state of the stations data.
         New/updated data is placed into station_dict"""

        self.station_dict['METAR'] = ''
        self.station_dict['TAF'] = ''

        if icao is not '':

            try:
                self.metar = new_metar
                self.metar_time = metar_time
                self.taf = new_taf
                self.taf_time = taf_time

                if self.metar is not '':
                    start_icao = icao_dict['ICAO']
                    start_time = icao_dict['METAR_TIME']
                    new_time = self.metar_time
                    current_colour = icao_dict['LATEST_COLOUR']

                    self.station_dict['ICAO'] = icao
                    self.station_dict['METAR_TIME'] = self.metar_time
                    self.station_dict['METAR'] = self.metar
                    self.station_dict['LATEST_COLOUR'] =\
                        metar_tools.get_colourstate_nbr(self.metar)

                    if new_time != start_time and start_icao == icao:
                        """Message times are different, put the old latest 
                        colour state into PREV_COLOUR If ICAO has been 
                        changed, don't swap over the PRE and LATEST colour 
                        states If message times are different change the 
                        NEW_METAR attribute to 1 - used for colour state
                        change alerts"""
                        self.station_dict['PREV_COLOUR'] = current_colour
                        self.station_dict['NEW_METAR'] = True

                    else:
                        """Take account of icao being changed in one of the 
                        input fields. In effect we are starting
                        again with monitoring this icao so set 
                        previous colour state to zero (grey)"""
                        if start_icao != icao:
                            self.station_dict['PREV_COLOUR'] = 0
                            self.station_dict['NEW_METAR'] = False

                        self.station_dict['NEW_METAR'] = False

                    if self.taf is not '':
                        self.station_dict['TAF'] = self.taf
                        self.station_dict['TAF_TIME'] = self.taf_time
                        self.station_dict['TAF_MIN_COLOUR'] = \
                            metar_tools.get_colourstate_nbr(self.taf)
                        self.taf_cnl = str(self.taf).find('CNL') == -1
                        self.taf_cnl = True

                    # Check if the METAR colour state is lower than the
                    # lowest TAF colour state and flag appropriately
                    # 2 if no TAF available, 1 if TAF bust, 0 if TAF
                    # is available and covers minimum colour state in
                    # latest METAR. If TAF is cancelled set status to 2.
                    if self.taf is '' or self.taf_cnl:
                        self.station_dict['TAF_STATUS'] = 2
                    elif self.station_dict['LATEST_COLOUR'] \
                            < self.station_dict['TAF_MIN_COLOUR']:
                        self.station_dict['TAF_STATUS'] = 1
                    else:
                        self.station_dict['TAF_STATUS'] = 0

            except AttributeError:
                """If no metar is found for the specified ICAO, just set 
                the ICAO field of the object. Need to do this
                otherwise the ICAO disappears from the window field"""
                self.station_dict['ICAO'] = icao

        else:
            """If the ICAO has been removed from the window field, set a 
            blank dictionary for this ICAO fields object"""
            self.station_dict = {'ICAO': '', 'METAR_TIME': '', 'METAR': '',
                                 'PREV_COLOUR': 0, 'LATEST_COLOUR': 0,
                                 'TAF_TIME': '', 'TAF': '',
                                 'TAF_MIN_COLOUR': 0, 'TAF_STATUS': 2,
                                 'NEW_METAR': True}
