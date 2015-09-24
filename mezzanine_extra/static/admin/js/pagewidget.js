jQuery(function () {
    jQuery('.pagewidget').on('change', function () {
        var $this = jQuery(this);
        var input = jQuery('#' + $this.attr('data-input-id')).val($this.val());
    });
});