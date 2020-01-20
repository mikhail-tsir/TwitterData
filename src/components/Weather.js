import React from "react";

const Weather = props => (
    <div className="weather_result">    
        {props.sentiment_avg && 
        <p className="weather__key">Average sentiment:
            <span className="weather__value"> {props.sentiment_avg}</span>
        </p>}

        {props.pos && 
        <p className="weather__key">Key words from positive tweets:
            <span className="weather__value"> {props.pos}</span>
        </p>}

        {props.neg && 
        <p className="weather__key">Key words from negative tweets:
            <span className="weather__value"> {props.neg}</span>
        </p>}

        {props.error && 
        <p className="weather__key">Error:
            <span className="weather__error"> {props.error}</span>
        </p>}
    </div>
);

export default Weather;
