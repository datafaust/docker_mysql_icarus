class StateVectors(SVMixin):
    """Plots the state vectors returned by OpenSky REST API."""

    def __init__(self, data: pd.DataFrame, opensky: "OpenSky") -> None:
        super().__init__(data)
        self.opensky = opensky

    def __getitem__(self, identifier: str):
        icao24 = self.data.query(
            "callsign == @identifier or icao24 == @identifier"
        ).icao24.item()
        return self.opensky.api_tracks(icao24)

def api_states(
        self,
        own: bool = False,
        bounds: Union[
            BaseGeometry, Tuple[float, float, float, float], None
        ] = None,
    ) -> StateVectors:
        """Returns the current state vectors from OpenSky REST API.
        If own parameter is set to True, returns only the state vectors
        associated to own sensors (requires authentication)
        bounds parameter can be a shape or a tuple of float.
        Official documentation
        ----------------------
        Limitiations for anonymous (unauthenticated) users
        Anonymous are those users who access the API without using credentials.
        The limitations for anonymous users are:
        Anonymous users can only get the most recent state vectors, i.e. the
        time parameter will be ignored.  Anonymous users can only retrieve data
        with a time resultion of 10 seconds. That means, the API will return
        state vectors for time now − (now mod 10)
        Limitations for OpenSky users
        An OpenSky user is anybody who uses a valid OpenSky account (see below)
        to access the API. The rate limitations for OpenSky users are:
        - OpenSky users can retrieve data of up to 1 hour in the past. If the
        time parameter has a value t < now−3600 the API will return
        400 Bad Request.
        - OpenSky users can retrieve data with a time resultion of 5 seconds.
        That means, if the time parameter was set to t , the API will return
        state vectors for time t−(t mod 5).
        """

        what = "own" if (own and self.auth is not None) else "all"

        if bounds is not None:
            try:
                # thinking of shapely bounds attribute (in this order)
                # I just don't want to add the shapely dependency here
                west, south, east, north = bounds.bounds  # type: ignore
            except AttributeError:
                west, south, east, north = bounds

            what += f"?lamin={south}&lamax={north}&lomin={west}&lomax={east}"

        c = self.session.get(
            f"https://opensky-network.org/api/states/{what}", auth=self.auth
        )
        c.raise_for_status()
        r = pd.DataFrame.from_records(
            c.json()["states"], columns=self._json_columns
        )
        r = r.drop(["origin_country", "spi", "sensors"], axis=1)
        r = r.dropna()

        r = self._format_dataframe(r)
        r = self._format_history(r)

        return StateVectors(r, self)