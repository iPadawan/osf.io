/*
 * Maintains the base class for knockoutJS form ViewModels
 */
'use strict';

var ko = require('knockout');

var $osf = require('osfHelpers');
var oop = require('js/oop');

var ValidationError = oop.extend(Error, {
    constructor: function (messages, header, level) {
        this.super.constructor.call(this);
        this.messages = messages || [];
        this.header = header || 'Error';
        this.level = level || 'warning';
    }
});

var FormViewModel = oop.defclass({
    constructor: function() {},
    isValid: function() {
        throw new Error('FormViewModel subclass must implement isValid');
    },
    submit: function() {
        try {
            this.isValid();
            return true; // Allow form to submit normally
        } catch (err) {
            if (err instanceof ValidationError) {
                for (var i = 0; i < err.messages.length; i++) {
                    $osf.growl(
                        err.header,
                        err.messages[i],
                        err.level
                    );
                }
                return false; // Stop form submission
            } else {
                throw err;
            }
        }
    }
});


module.exports = {
    FormViewModel: FormViewModel,
    ValidationError: ValidationError
};