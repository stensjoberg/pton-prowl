import React, { Component } from 'react';
import Radium from 'radium';
import { styles } from './styles';
import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';

const dayreps = new Map([
    ['monday','Mon'],
    ['tuesday','Tues'],
    ['wednesday','Wed'],
    ['thursday','Thurs'],
    ['friday','Fri'],
    ['saturday','Sat'],
    ['sunday','Sun']
])

const hourreps = new Map([
    [0,'12am'],
    [1,'1am'],
    [2,'2am'],
    [3,'3am'],
    [4,'4am'],
    [5,'5am'],
    [6,'6am'],
    [7,'7am'],
    [8,'8am'],
    [9,'9am'],
    [10,'10am'],
    [11,'11am'],
    [12,'12pm'],
    [13,'1pm'],
    [14,'2pm'],
    [15,'3pm'],
    [16,'4pm'],
    [17,'5pm'],
    [18,'6pm'],
    [19,'7pm'],
    [20,'8pm'],
    [21,'9pm'],
    [22,'10pm'],
    [23,'11pm']
])

const AVAIL = true

class Availability extends Component {


    state = {
        availability: this.props.data,
        changeTo: AVAIL,
        mouseIsDown: false

    };

    handleSumbit = async (event) => {
        return true
    }

    handleMouseDown = async (day, hour, value, e) => {
        const mouseIsDown = true
        const changeTo = !value

        await this.setState({
            mouseIsDown,
            changeTo
        })

        this.handleMouseEnter(day, hour, value, e)
    }

    handleMouseUp = (e) => {
        const mouseIsDown = false

        this.setState({
            mouseIsDown
        })
    }

    handleMouseEnter = (day, hour, value, e) => {
        if (this.state.mouseIsDown) {
            const availability = this.state.availability
            availability[day][hour] = this.state.changeTo
            this.setState({
                availability
            });
        }
    }

    render() {
        if (this.state.availability === undefined) {
            console.log("state undefined")
            return false
        }
        else {
            return (
              <div className="right">
                <div className="flexcontainer hor" onMouseUp={(e) => this.handleMouseUp(e)}>
                {Object.keys(this.state.availability).map((day) => (
                    <div className="flexcontainer vert" key={day}>
                    <h5>{dayreps.get(day)}</h5>
                    {this.state.availability[day].map((value, hour) => (
                        <button className="times" key={day+hour}
                                onMouseEnter={(e) => this.handleMouseEnter(day, hour, value, e)}
                                onMouseDown={(e) => this.handleMouseDown(day, hour, value, e)}
                                style={Object.assign({},
                                    value && styles.available,
                                    !value && styles.unavailable
                                )}>
                            {hourreps.get(hour)}
                        </button>

                    ))}
                    </div>
                ))}
                </div>
              </div>
            )
        }
    }
}

export default Radium(Availability)
