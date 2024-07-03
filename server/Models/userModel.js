const mongoose = require('mongoose');
const JWT = require('jsonwebtoken');
const bcrypt = require('bcrypt');


const userSchema = mongoose.Schema({
    username: {
        type: String,
        required: [true, 'user name is required'],
        trim: [true],
        unique: [true, 'username already taken'],
        validate: {
            validator: function (v) {
                return /^[a-zA-Z0-9_]+$/.test(v);
            },
            message: props => `${props.value} is not a valid username!`
        }
    },
    email: {
        type: String,
        required: true,
        unique: [true, 'already registered']
    },

    password: {
        type: String,
        required: true
    },
    forgotPasswordToken: {
        type: String
    },
    forgotPasswordExpiryDate: {
        type: Date
    },
}, {
    timestamps: true
}
);

userSchema.pre('save', async function (next) {
    if (!this.isModified('password')) {
        return next();
    }
    this.password = await bcrypt.hash(this.password, 10);
    return next();
})

userSchema.methods = {
    jwtToken() {
        return JWT.sign(
            { id: this._id, email: this.email },
            process.env.SECRET,
            { expiresIn: '24h' }
        )
    }
}


const userModel = mongoose.model('user', userSchema);

module.exports = { userModel };



