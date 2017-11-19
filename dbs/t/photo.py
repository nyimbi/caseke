    def ViewName(self):
        return self.__class__.__name__ +'View'

    # @property
    def photo_img(self):
        im = ImageManager()
        vn = self.ViewName()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    # @property
    def photo_img_thumbnail(self):
        im = ImageManager()
        vn = self.ViewName()
        if self.photo:
            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +
                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +
                        '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +
                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


    # @property
    def print_button(self):
        vn = self.ViewName()
        #pdf = render_pdf(url_for(vn, pk=str(self.id)))
        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))
        #response = make_response(pdf)
        #response.headers['Content-Type'] = 'application/pdf'
        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'

        return Markup(
            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+
            'title="Print">' +
            '<i class="fa fa-edit"></i>' +
            '</a>')


    # @property
    def audio_play(self):
        vn = self.ViewName()
        return Markup(
                '<audio controls autoplay>' +
                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +
                'Your browser does not support the audio element.' +
                '</audio>'
                )
    # edit_form_extra_fields = {'field2': TextField('field2',
    #                             widget=BS3TextFieldROWidget())}
