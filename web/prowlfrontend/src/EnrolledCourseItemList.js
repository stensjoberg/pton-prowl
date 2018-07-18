import React, { Component } from 'react'
import Radium from 'radium'
import CourseItem from './CourseItem'
import { Link } from 'react-router-dom'
import { getUser, getCourse, getObjectsFromLinks } from './helper.js'
import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';

class EnrolledCourseItemList extends Component {
    state = {
        courses: [],
    }

    async componentDidMount() {
        const user = await getUser()
        const courselinks = user.courses
        const courses = await getObjectsFromLinks(courselinks)

        this.setState({
            courses
        })
        console.log(this.state.courses)
    }

    render() {
        return (
            <div className="flexcontainer vert">
            <h3>Enrolled Courses</h3>
            {this.state.courses.map((item, i) => (
                <Link to={'/course/'+item.id} key={item.id}>
                <CourseItem
                id={item.id}
                title={item.title}
                i={i}
                add={false}
                />
                </Link>
            ))}
            </div>
        )
    }
}

export default Radium(EnrolledCourseItemList)
