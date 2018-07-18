import React, { Component } from 'react';
import Radium from 'radium';
import { styles } from './styles';
import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';

const dayreps = new Map([
    ['monday','Mond'],
    ['tuesday','Tues'],
    ['wednesday','Wedn'],
    ['thursday','Thur'],
    ['friday','Fri'],
    ['saturday','Sat'],
    ['sunday','Sun']
])

const hourreps = new Map([
    [0,'00:00'],
    [1,'01:00'],
    [2,'02:00'],
    [3,'03:00'],
    [4,'04:00'],
    [5,'05:00'],
    [6,'06:00'],
    [7,'07:00'],
    [8,'08:00'],
    [9,'09:00'],
    [10,'10:00'],
    [11,'11:00'],
    [12,'12:00'],
    [13,'13:00'],
    [14,'14:00'],
    [15,'15:00'],
    [16,'16:00'],
    [17,'17:00'],
    [18,'18:00'],
    [19,'19:00'],
    [20,'20:00'],
    [21,'21:00'],
    [22,'22:00'],
    [23,'23:00'],
    [24,'24:00']
])

const AVAIL = true
const UNAVAIL = false

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
                <div className="flexcontainer hor" onMouseUp={(e) => this.handleMouseUp(e)}>
                {Object.keys(this.state.availability).map((day) => (
                    <div className="flexcontainer vert" key={day}>
                    <h4>{dayreps.get(day)}</h4>
                    {this.state.availability[day].map((value, hour) => (
                        <button key={day+hour}
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
            )
        }
    }
}

export default Radium(Availability)
