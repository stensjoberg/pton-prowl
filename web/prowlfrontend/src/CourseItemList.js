import React, { Component } from 'react'
import Radium from 'radium'
import CourseItem from './CourseItem'
import { Link } from 'react-router-dom'
import { getUser, getCourse, getAllCourses, getCoursesFromLinks } from './helper.js'
import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';

const ENROLL = true
const UNENROLL = false

class CourseItemList extends Component {
    state = {
        searchString: '',
        availCourses: [],
        filteredAvailCourses: [],
        enrolledCourses: []
    }

    handleSearch = async (value) => {
        const searchString = value.toLowerCase()
        let filteredAvailCourses = this.state.availCourses
        filteredAvailCourses = this.state.availCourses.filter(elem =>
            elem.title.toLowerCase().search(
                searchString) !== -1
        )
        this.setState({
            searchString,
            filteredAvailCourses
        })
    }

    handleChange = async (id, change) => {
        let availCourses = this.state.availCourses
        let enrolledCourses = this.state.enrolledCourses
        if(change === ENROLL) {
            enrolledCourses.unshift(availCourses.find(elem => elem.id === id))
            availCourses = availCourses.filter(elem => elem.id !== id)
        }
        else { // change is UNENROLL
            availCourses.unshift(enrolledCourses.find(elem => elem.id === id))
            enrolledCourses = enrolledCourses.filter(elem => elem.id !== id)
        }

        await this.setState({
            availCourses,
            enrolledCourses
        })

        this.handleSearch(this.state.searchString)
    }
    async componentDidMount() {

        const allCourses = await getAllCourses()
        const user = await getUser()
        const enrolledCourses = await getCoursesFromLinks(user.courses)

        let availCourses = []
        allCourses.map((course) => {
            if (!enrolledCourses.some(ec => ec.id === course.id)) {
                availCourses.push(course)
            }
        })
        this.setState({
            availCourses,
            enrolledCourses,
            filteredAvailCourses: availCourses
        })
    }

    render() {
        return (
            <div className="flexcontainer vert" className="left">
            <h3>Enrolled Courses</h3>
            {this.state.enrolledCourses.map((item, i) => (
                <Link to={'/course/'+item.id} key={item.id}>
                <CourseItem
                id={item.id}
                title={item.title}
                i={i}
                change={UNENROLL}
                onChange={this.handleChange}
                />
                </Link>
            ))}
            <h3>Available Courses</h3>
            <form><fieldset>
            <input type="text" placeholder="Search" onChange={(e) => this.handleSearch(e.target.value)}/>
            </fieldset></form>
            {this.state.filteredAvailCourses.map((item, i) => (
                <Link to={'/course/'+item.id} key={item.id}>
                <CourseItem
                id={item.id}
                title={item.title}
                i={i}
                change={ENROLL}
                onChange={this.handleChange}
                />
                </Link>
            ))}
            </div>
        )
    }
}

export default Radium(CourseItemList)
